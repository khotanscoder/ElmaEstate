from django.contrib import admin

# Register your models here.
from .models import Estate, Blog

admin.site.register(Estate)
admin.site.register(Blog)


