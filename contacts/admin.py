from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('email',)
    ordering = ('last_name', 'first_name')
    fields = ('first_name', 'last_name', 'email', 'phone_number', 'address')
