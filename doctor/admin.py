from django.contrib import admin
from .models import Doctor,Specialization,Designation,AvailableTime,Review
# Register your models here.

class DoctorAdmin(admin.ModelAdmin):

    list_display=['user','designation','specialization','available_time','fee']

    '''def first_name(self,obj):
        return obj.user.first_name
    
    def last_name(self,obj):
        return obj.user.last_name'''
    def user(self,obj):
        return f"{obj.user.user}"
    
    def designation(self,obj):
        return f"{obj.user.designation}"
    
    def specialization(self,obj):
        return f"{obj.user.specialization}"

    def available_time(self,obj):
        return obj.user.available_time
    
    def fee(self,obj):
        return f"{obj.user.fee}"

# for creating automatic slug start
class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',),}

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',),}

# for creating automatic slug end

class ReviewAdmin(admin.ModelAdmin):
    list_display=['reviewer','doctor','time']

    def reviewer(self,obj):
        return f"{obj.reviewer}"
    def doctor(self,obj):
        return f"{obj.doctor}"
    def time(self,obj):
        return f"{obj.created}"

admin.site.register(Specialization,SpecializationAdmin)
admin.site.register(Designation,DesignationAdmin)
admin.site.register(AvailableTime)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Review,ReviewAdmin)
