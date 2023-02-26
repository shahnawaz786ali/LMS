from django.contrib import admin
from users.models import Contact, user_profile_parent,user_profile_principal,user_profile_school,user_profile_student,user_profile_teacher,User

# Register your models here.
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(user_profile_teacher)
admin.site.register(user_profile_student)
admin.site.register(user_profile_principal)
admin.site.register(user_profile_school)
admin.site.register(user_profile_parent)