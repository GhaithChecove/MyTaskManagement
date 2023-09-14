from django.contrib import admin
from . import models as m
# Register your models here.

admin.site.register(m.Active)
admin.site.register(m.Stuff)
admin.site.register(m.Suspended)
admin.site.register(m.Category)
admin.site.register(m.Finished)
admin.site.register(m.Task)

