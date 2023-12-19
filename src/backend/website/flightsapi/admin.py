from django.contrib import admin
from .models import Flight

# Makes table accessible from admin page
admin.site.register(Flight)