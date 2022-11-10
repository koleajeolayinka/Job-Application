from django.contrib import admin
from app.models import JobPost


class JobAdmin(admin.ModelAdmin):
    list_display = ("__str__", "title", "salary", "date")
    list_filter = ("salary", "date")
    search_fields = ("title", "salary")
    search_help_text = "write in your query and hit enter"
    # fields= ["title"]
    # exclude= ("title",)
    fieldsets = (
        (
            "Basic Information", {'fields':("title", "description",)
        }),
        ("More Information", 
        {
        "classes": ("collapse",),

        "fields":("expire", "salary", "url",)
        }),
    )


# Register your models here.
admin.site.register(JobPost, JobAdmin)
