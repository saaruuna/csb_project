from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Message
from django.db.models import Q

# Create your views here.

@login_required
def addView(request):
	target = User.objects.get(username=request.POST.get('to'))
	Message.objects.create(source=request.user, target=target, content=request.POST.get('content'))
	return redirect('/')

@login_required
@csrf_exempt
def homePageView(request):
	messages = Message.objects.filter(Q(source=request.user) | Q(target=request.user))

	users = User.objects.exclude(pk=request.user.id)
	sql = 'SELECT * FROM pages_message WHERE (source_id=' + str(request.user.id) + ' OR target_id=' + str(request.user.id) + ')'

	if request.GET.get('search'):
		sql += " AND content LIKE '%" + str(request.GET.get('search')) + "%'"
		messages = Message.objects.raw(sql)

	return render(request, 'pages/index.html', {'msgs': messages, 'users': users,})

@login_required
def deleteView(request):
	m = Message.objects.get(pk=request.POST.get('id'))
	m.delete()
	return redirect('/')
