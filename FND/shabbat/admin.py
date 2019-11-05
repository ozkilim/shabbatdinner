from django.contrib import admin
from .models import User, GroupA, GroupB, GroupOfEight


# Register your models here.

admin.site.register(User)
admin.site.register(GroupA)
admin.site.register(GroupB)
admin.site.register(GroupOfEight)

