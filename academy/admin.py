from django.contrib import admin

# Register your models here.
from.models import Courses, Blog, Documentation

admin.site.register(Courses)
admin.site.register(Blog)
admin.site.register(Documentation)