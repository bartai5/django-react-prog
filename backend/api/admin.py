from django.contrib import admin
from .models import Project

# Register your models here.
db_list = [
    Project,
]

admin.site.register(db_list)
