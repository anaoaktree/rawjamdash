from django.contrib import admin

# Register your models here.


from django.contrib import admin
from hello.models import SubUser

class SubUserAdmin(admin.ModelAdmin):
    pass





admin.site.register(SubUser, SubUserAdmin)