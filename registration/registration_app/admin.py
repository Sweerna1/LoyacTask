from django.contrib import admin

from .models import Program, Applicant, Staff, DiscountCode

admin.site.register(Program)
admin.site.register(Applicant)
admin.site.register(Staff)
admin.site.register(DiscountCode)
