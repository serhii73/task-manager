from django.contrib import admin

from .models import Category, LabelTask, Task

admin.site.register(Category)
admin.site.register(LabelTask)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['author', 'name_task', 'description_task', 'category_task', 'created_date',
                    'deadline_task']
