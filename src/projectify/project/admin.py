from django.contrib import admin

from project.models import (
    
    Project,
    Contractor,
    Review

)


admin.site.register(Project)
admin.site.register(Contractor)
admin.site.register(Review)