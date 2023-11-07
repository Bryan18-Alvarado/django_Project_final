from django.contrib import admin

# Register your models here.
from.models import Courses, Blog, Documentation,Contact_us

admin.site.register(Courses)
admin.site.register(Blog)
admin.site.register(Documentation)
admin.site.register(Contact_us)