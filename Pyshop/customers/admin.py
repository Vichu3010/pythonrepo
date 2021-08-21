from django.contrib import admin
from .models import Customers


class CustomersAdmin(admin.ModelAdmin):
    list_display = ('Id','first_name','last_name','contact','address')


admin.site.register(Customers,CustomersAdmin)