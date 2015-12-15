from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import RequestContext
from django.utils import timezone

from .models import User, Will, Moment

import logging
from service import regist_user_email, create_will, create_moment, calc_md5

# Create your views here.

logger = logging.getLogger(__name__)

def index(request):
    logger.info(__name__)
    return HttpResponse('hello index')

def login_page(request):
    context = {}
    return render(request, 'will/login.html', context)

def regist_page(request):
    context = {}
    return render(request, 'will/regist.html', context)

def login(request):
    email = request.POST['email']
    password = request.POST['passwd']
    try:
        user = User.objects.get(email = email)
        if not user.password == calc_md5(password):
            raise ValueError('password is incorrect')
    except:
        return HttpResponseBadRequest('login failed')
    response = redirect(reverse('wills:will_list', args=[user.id]))
    response.set_cookie('userid', user.id)
    return response

def regist(request):
    pwd = request.POST.get('passwd')
    if not len(pwd.strip()) >= 6 or not len(pwd.strip()) <= 12:
        return HttpResponseBadRequest('password illegal')
    pwd = calc_md5(pwd)
    (user, first_create) = regist_user_email(request.POST.get('email'), 
            pwd)
    logger.info(user, first_create)
    logger.info(first_create)
    if not first_create:
        return HttpResponseBadRequest('the email is being used')
    response = redirect(reverse('wills:will_list', args=[user.id]))
    response.set_cookie('userid', user.id)
    return response

def wills(request, userid):
    if not userid == request.COOKIES.get('userid'):
        return HttpResponseBadRequest('not login')
    context = {}
    m_wills = Will.objects.filter(user__id=userid)
    context['wills'] = m_wills
    context['userid'] = userid
    return render_to_response('will/main.html', 
            context_instance=RequestContext(request, context))

def moments(request, willid):
    context = {}
    userid = request.COOKIES.get('userid')
    try:
        will = Will.objects.get(pk=willid)
        moments = will.moment_set.all()
        if not str(will.user.id) == str(userid):
            raise ValueError('will and user not match')
    except:
        return HttpResponseBadRequest('%s\t%s' % (will.user.id, userid))
    context = {}
    context['moments'] = moments
    context['willid'] = willid
    return render_to_response('will/moments.html',
            context_instance=RequestContext(request, context))



def will_create_page(request):
    if '' == request.COOKIES.get('userid'):
        return HttpResponseBadRequest('not login')
    context = {}
    # return render(request, 'will/create_will.html', context)
    return render_to_response('will/create_will.html', 
            context_instance=RequestContext(request, context))


def moment_create_page(request, willid):
    if '' == request.COOKIES.get('userid'):
        return HttpResponseBadRequest('not login')
    context = {}
    context['willid'] = willid
    return render_to_response('will/create_moment.html', 
            context_instance=RequestContext(request, context))


def moment_create(request, willid):
    try:
        will = Will.objects.get(pk=willid)
    except:
        return HttpResponseBadRequest('will error')
    create_moment(request.POST.get('moment_text'), 
            '',
            timezone.now(),
            will)
    response = redirect(reverse('wills:moment_list', args=[will.id]))
    return response


def will_create(request):
    userid = request.COOKIES.get('userid')
    try:
        user = User.objects.get(pk=userid)
    except:
        return HttpResponseBadRequest('userid illegal')
    create_will(request.POST.get('will_text'), 
            timezone.now(), 
            '', 
            user)
    response = redirect(reverse('wills:will_list', args=[user.id]))
    response.set_cookie('userid', user.id)
    return response

