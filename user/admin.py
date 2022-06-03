from django.contrib import admin
from .models import User,Policy,Page,Visit
# Register your models here.


admin.site.register(User)
admin.site.register(Policy)
admin.site.register(Page)
admin.site.register(Visit)
