from django.contrib import admin
from .models import Dsu

class DsuAdmin(admin.ModelAdmin):

    list_display=('name','price','stocks')
admin.site.register(Dsu,DsuAdmin)
