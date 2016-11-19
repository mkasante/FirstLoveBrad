from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from member.models import Member
import re

# Create your views here.
@login_required
def index(request):
	context = {}

	return render (request, 'index.html', context)


@login_required
def all_members(request):
	members = Member.objects.all()
	alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	context = {
		'members': members,
		'alphabets': alphabets
	}

	return render (request, 'all_members.html', context)


@login_required
def _sort_members_by_alphabet(request, alphabet):
	pattern = re.compile(r"^([a-zA-Z])$")

	if pattern.match(alphabet):
		members = Member.objects.filter(name__istartswith = alphabet)
	else:
		members = Member.objects.all()

	context = {
		'members': members,
	}

	return render (request, '_partial/sort_by_alphabet.html', context)