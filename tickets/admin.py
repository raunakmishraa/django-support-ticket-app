from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import custom_user_model,global_settings,ticket_model

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('phone','is_email_verified')}),

# Register your models here.
@admin.register(custom_user_model)
class users_view(UserAdmin):
	list_display = ('first_name','last_name','username', 'phone','is_email_verified')


@admin.register(global_settings)
class GlobalSettings(admin.ModelAdmin):
	list_display = ('email','phone','fb_link', 'insta_link')
	ordering = ('email','phone','fb_link', 'insta_link',)
	search_fields = ('email','phone','fb_link', 'insta_link')

@admin.register(ticket_model)
class support_ticket_model(admin.ModelAdmin):
	list_display = ('raised_by','subject','issue', 'priority','ticket_number','status')
	ordering = ('priority','raised_by','subject','issue', 'ticket_number')
	search_fields = ('raised_by','subject','issue', 'priority','ticket_number')

'''
class EmployeeAdmin(UserAdmin):
    pass

admin.site.register(custom_user_model, EmployeeAdmin)
'''