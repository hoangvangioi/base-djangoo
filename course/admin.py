from django.contrib import admin
from .models import Course

# Register your models here.


from parler.admin import TranslatableAdmin

admin.site.register(Course, TranslatableAdmin)