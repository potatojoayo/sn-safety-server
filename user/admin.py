# user/admin.py

from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    
		# admin사이트의 user에서 보여질 속성들
    list_display = (
        'email',
        'name',
        'phone',
        'date_joined'
    )

    list_display_links = (
        'email',
        'name'
    )
