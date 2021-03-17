from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Kid

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        *BaseUserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'is_kid',
                    'is_parent',
                ),
            },
        ),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Kid)
# Register your models here.
