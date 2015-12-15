from django.contrib import admin
from .models import User, Will, Moment

# Register your models here.

admin.site.register(User)


admin.site.register(Will)
admin.site.register(Moment)

