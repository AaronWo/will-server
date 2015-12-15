from django.db import models
from models import User, Will, Moment

import hashlib

def regist_user_email(email, pwd):
    (user, first_create) = User.objects.get_or_create(email=email, password=pwd)
    return (user, first_create)

def regist_user_wechat(wechat_id):
    pass

def create_will(will_text, image_url, create_date, user):
    will = Will(will_text = will_text,
            image_url = image_url,
            create_date = create_date,
            update_date = create_date,
            user = user)
    will.save()
    
def create_moment(p_moment_text, p_image_url, p_create_date, p_will):
    moment = Moment(moment_text = p_moment_text,
            create_date = p_create_date,
            image_url = p_image_url,
            will = p_will)
    moment.save()

def calc_md5(src):
    md5_obj = hashlib.md5()
    md5_obj.update(src)
    return md5_obj.hexdigest()
