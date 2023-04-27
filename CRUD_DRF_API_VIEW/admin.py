from django.contrib import admin
from .models import studentModel
# Register your models here.

@admin.register(studentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']