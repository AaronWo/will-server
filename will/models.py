from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=12)

    def __unicode__(self):
        return self.email


class Will(models.Model):
    will_text = models.TextField()
    image_url = models.TextField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.will_text


class Moment(models.Model):
    moment_text = models.TextField()
    create_date = models.DateTimeField()
    image_url = models.TextField()
    will = models.ForeignKey(Will)

    def __unicode__(self):
        return self.moment_text
