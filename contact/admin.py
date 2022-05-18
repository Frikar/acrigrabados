from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    search_fields =  ('email','date')
    list_display = ('name', 'email', 'phone','date', 'msg')
    list_filter= ['email','date']  

admin.site.register(Contact, ContactAdmin)