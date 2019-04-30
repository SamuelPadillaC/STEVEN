from django.contrib import admin
from django.http import HttpRequest

from .models import College, Student, ISD
from . import views
from . import email_info


class EmailTrigger(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super(EmailTrigger, self).save_model(request, obj, form, change)
        email_info.recepient = [obj.ISD_Email]
        email_info.school = obj.Name
        email_info.slots = obj.Student_Slots
        return views.mail(request)


admin.site.register(College, EmailTrigger)
admin.site.register(Student)
admin.site.register(ISD)
