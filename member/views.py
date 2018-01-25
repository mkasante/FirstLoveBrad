from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from member.models import Member, Attendance, Gender
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.urlresolvers import reverse
import datetime
import re
import operator
from firstlove.helpers.getlocation import getdata

# Create your views here.


def _(text):
    return text.strip()


@login_required
def index(request):
    context = {}

    return render(request, 'member/index.html', context)


@login_required
def all_members(request):
    members = Member.objects.all()
    alphabets = sorted(set([x.name[0] for x in members]))
    membership_status = Attendance.objects.all()
    gender = Gender.objects.all()

    context = {
        'members': members,
        'alphabets': alphabets,
        'membership_status': membership_status,
        'gender': gender
    }

    return render(request, 'member/all_members.html', context)


@login_required
def member_info(request, name):
    member = Member.objects.get(name__iexact=name)

    context = {
        'member': member
    }

    return render(request, 'member/member_info.html', context)


@login_required
def shepherd_list(request):
    shepherds = User.objects.order_by('-last_login')

    context = {
        'shepherds': shepherds
    }

    return render(request, 'member/shepherd_list.html', context)


@login_required
def shepherd_info(request, name):
    shepherd = User.objects.get(username__iexact=name)
    members = Member.objects.filter(shepherd__username__iexact=name)

    context = {
        'shepherd': shepherd,
        'members': members
    }

    return render(request, 'member/shepherd_info.html', context)


@login_required
def close_proximity_members(request, post_code, mode="walking"):
    closest = []
    members = Member.objects.exclude(Q(attendance_status__status__iexact="evangelism"),
                                     Q(attendance_status__status__iexact="outreach"),
                                     Q(attendance_status__status__iexact="relocated")).filter(post_code__istartswith=post_code[0])

    post_codes = [x.post_code for x in members if x.post_code]
    names = [x.name for x in members]

    result = []

    try:
        closest = getdata(post_code, post_codes, mode)
        for i in range(len(closest)):
            result.append([names[i], closest[i][0], closest[i]
                           [1], closest[i][2], closest[i][3]])

        data = sorted(result, key=operator.itemgetter(4))
    except:
        data = ""

    context = {
        'close_members': data,
        'mode': mode,
        'near_count': len(data),
        'post_code': post_code
    }
    return render(request, 'member/close_proximity_members.html', context)


@login_required
def close_proximity_followup(request, shepherd, post_code, mode="walking"):
    closest = []
    members = Member.objects.exclude(Q(attendance_status__status__iexact="evangelism"),
                                     Q(attendance_status__status__iexact="outreach"),
                                     Q(attendance_status__status__iexact="relocated")).filter(Q(shepherd__username__iexact=shepherd), Q(post_code__istartswith=post_code[0]))

    post_codes = [x.post_code for x in members if x.post_code]
    names = [x.name for x in members]

    result = []

    try:
        closest = getdata(post_code, post_codes, mode)
        for i in range(len(closest)):
            result.append([names[i], closest[i][0], closest[i]
                           [1], closest[i][2], closest[i][3]])

        data = sorted(result, key=operator.itemgetter(4))
    except:
        data = ""

    context = {
        'close_members': data,
        'mode': mode,
        'near_count': len(data),
        'post_code': post_code
    }
    return render(request, 'member/close_proximity_members.html', context)

# Partial


@login_required
def _list_members_by_alphabet(request, alphabet):
    pattern = re.compile(r"^([a-zA-Z])$")

    if pattern.match(alphabet):
        members = Member.objects.filter(name__istartswith=alphabet)
    else:
        members = Member.objects.all()

    context = {
        'members': members
    }

    return render(request, '_partial/member_data.html', context)


@login_required
def _list_members_by_status(request, status):
    pattern = re.compile(r"^([\w\s\d\.-_]+)$")

    if pattern.match(status) and status != "ALL":
        attendance = Attendance.objects.get(status__iexact=status).status
        members = Member.objects.filter(
            attendance_status__status__iexact=attendance)
    else:
        members = Member.objects.all()

    context = {
        'members': members
    }

    return render(request, '_partial/member_data.html', context)


@login_required
def _list_members_by_gender(request, gender):
    pattern = re.compile(r"^([\w]+)$")

    if pattern.match(gender) and gender != "ALL":
        gender = Gender.objects.get(gender__iexact=gender).gender
        members = Member.objects.filter(gender__gender__iexact=gender)
    else:
        members = Member.objects.all()

    context = {
        'members': members
    }

    return render(request, '_partial/member_data.html', context)


@login_required
def signup_firsttimer(request):
    last5years = datetime.datetime.now() - datetime.timedelta(days=1825) 
    context = {
        "last5years": str(last5years).split(" ")[0]
    }
    if request.method == 'POST':
        post_data = request.POST.dict()

        gender = Gender.objects.get(id=_(post_data["gender"]))
        attendance = Attendance.objects.get(status__iexact="first timer")
        shepherd = User.objects.first()

        extra_info = "Invited by %s. %s" % (post_data["who_invited_you"], post_data["visiting_status"])
        member = Member.objects.create(
            name=_(post_data["name"]),
            gender=gender,
            mobile_no=_(post_data["mobile_no"]),
            email=_(post_data["email"]),
            date_of_birth=_(post_data["date_of_birth"]),
            address=_(post_data["address"]),
            post_code=_(post_data["post_code"]),
            first_attended=datetime.datetime.now(),
            attendance_status_id=attendance.id,
            shepherd_id=shepherd.id,
            extra_info=extra_info
        )

        return HttpResponseRedirect(reverse('member:all_members'))

    return render(request, "member/first_timer_signup.html", context)
