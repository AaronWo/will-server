#!/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse,HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from wechat_sdk import WechatBasic
from wechat_sdk.messages import TextMessage, ImageMessage, VideoMessage, LinkMessage, EventMessage
from wechat_sdk.exceptions import ParseError

WECHAT_TOKEN = 'melonstudio-will'
AppID = ''
AppSecret = ''

wechat_instance = WechatBasic(
    token = WECHAT_TOKEN,
    appid = AppID,
    appsecret = AppSecret
)

@csrf_exempt
def index(request):
    if request.method == 'GET':
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        if not wechat_instance.check_signature(
                signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponseBadRequest('Valid Failed')
        return HttpResponse(
                request.GET.get('echostr', ''), content_type='text/plain')
    else:
        try:
            wechat_instance.parse_data(data=request.body)
        except ParseError:
            return HttpResponseBadRequest('Invalid XML Data')
        
        message = wechat_instance.get_message()
        return process_request(message)

def process_request(message):
    if isinstance(message, TextMessage):
        response = process_text_request(message)
    elif isinstance(message, ImageMessage):
        response = process_image_request(message)
    elif isinstance(message, EventMessage):
        response = process_event_request(message)
    return HttpResponse(response, content_type = 'application/xml')

def process_text_request(message):
    response = wechat_instance.response_text(
            content = ('hahah hahaha hahah'))
    return response

def process_voice_request(message):
    pass

def process_image_request(message):
    pass

def process_link_request(message):
    pass

def process_event_request(message):
    if message.type == 'subscribe':
        response = process_subscribe(message)
    elif message.type == 'click':
        response = process_click(message)
    elif message.type == 'view':
        response = process_view(message)
    return response

def process_subscribe(message):
    response = wechat_instance.response_text(
            content = ('hahah hahaha hahah subscribe'))
    return response

def process_click(message):
    response = wechat_instance.response_text(
            content = ('hahah hahaha hahah click'))
    return response

def process_view(message):
    response = wechat_instance.response_text(
            content = ('hahah hahaha hahah view'))
    return response
