from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('student/', views.StudentSignUpView.as_view(), name="user_student"),
    path('parent/', views.ParentSignUpView.as_view(), name="user_parent"),
    path('teacher/', views.TeacherSignUpView.as_view(), name="user_teacher"),
    path('principal/', views.PrincipalSignUpView.as_view(), name="user_principal"),
    path('school/', views.SchoolSignUpView.as_view(), name="user_school"),
    path('login/',views.user_login, name="login"),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.register, name='register'),
    path('student_report/',views.studentreport, name="student_report")
]
