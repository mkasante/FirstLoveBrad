from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from member.models import Member, Attendance

import re


# Create your views here.
@login_required
def index(request):
	context = {}

	return render (request, 'member/index.html', context)


@login_required
def all_members(request):
	members = Member.objects.all()
	alphabets = sorted(set([x.name[0] for x in members]))
	membership_status = Attendance.objects.all()

	context = {
		'members': members,
		'alphabets': alphabets,
		'membership_status': membership_status
	}

	return render (request, 'member/all_members.html', context)

@login_required
def member_info(request, name):
	member = Member.objects.get(name__iexact= name)

	context = {
		'member': member
	}

	return render (request, 'member/member_info.html', context)

# Partial
@login_required
def _list_members_by_alphabet(request, alphabet):
	pattern = re.compile(r"^([a-zA-Z])$")

	if pattern.match(alphabet):
		members = Member.objects.filter(name__istartswith = alphabet)
	else:
		members = Member.objects.all()

	context = {
		'members': members
	}

	return render (request, '_partial/member_data.html', context)


@login_required
def _list_members_by_status(request, status):
	pattern = re.compile(r"^([\w\s\d\.-_]+)$")

	if pattern.match(status) and status != "ALL":
		attendance = Attendance.objects.get(status__iexact = status).status
		members = Member.objects.filter(attendance_status__status__iexact = attendance)
	else:
		members = Member.objects.all()

	context = {
		'members': members
	}

	return render (request, '_partial/member_data.html', context)