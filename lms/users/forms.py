from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from users.models import user_profile_student,user_profile_parent,user_profile_principal,user_profile_school,user_profile_teacher,User

class studentsignupform(UserCreationForm):
    email=forms.EmailField(required=True)
    First_Name=forms.CharField(required=True)
    Middle_Name=forms.CharField(required=False)
    Last_Name=forms.CharField(required=True)
    # dob=forms.DateField(required=False)
    grade=forms.CharField(required=True)
    school=forms.CharField(required=True)
    country=forms.CharField(required=False)
    state=forms.CharField(required=False)
    city=forms.CharField(required=False)

    class Meta(UserCreationForm.Meta):
        model=User

    def __init__(self, *args, **kwargs):
        super(studentsignupform, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None
        self.label_suffix = ""

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_student = True
        user.save()
        student = user_profile_student.objects.create(user=user)
        student.first_name=self.cleaned_data.get('First_Name')
        student.middle_name=self.cleaned_data.get('Middle_Name')
        student.last_name=self.cleaned_data.get('Last_Name')
        # student.dob=self.cleaned_data.get('dob')
        student.grade=self.cleaned_data.get('grade')
        student.school=self.cleaned_data.get('school')
        student.country=self.cleaned_data.get('country')
        student.state=self.cleaned_data.get('state')
        student.city=self.cleaned_data.get('city')

        # if len('password1') < 8:
        #     self._errors['password'] = self.error_class(['Password length should not be less than 8 characters'])
        student.save()
        return user

class parentsignupform(UserCreationForm):
    email=forms.EmailField(required=True)
    First_name=forms.CharField(required=True)
    Middle_name=forms.CharField(required=False)
    Last_name=forms.CharField(required=True)
    mobile=forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model=User

    def __init__(self, *args, **kwargs):
        super(parentsignupform, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None
        self.label_suffix = ""

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_parent=True
        user.save()
        parent=user_profile_parent.objects.create(user=user)
        parent.first_name=self.cleaned_data.get('First_name')
        parent.middle_name=self.cleaned_data.get('Middle_name')
        parent.last_name=self.cleaned_data.get('Last_name')
        parent.mobile=self.cleaned_data.get('mobile')
        parent.save()

        return parent

class teachersignupform(UserCreationForm):
    email=forms.EmailField(required=True)
    First_Name=forms.CharField(required=True)
    Middle_Name=forms.CharField(required=False)
    Last_Name=forms.CharField(required=True)
    mobile=forms.CharField(required=True)
    # dob=forms.DateField(required=True)
    grade=forms.CharField(required=False)
    school=forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model=User

    def __init__(self, *args, **kwargs):
        super(teachersignupform, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None
        self.label_suffix = ""

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_teacher = True
        user.save()
        teacher = user_profile_teacher.objects.create(user=user)
        teacher.first_name=self.cleaned_data.get('First_Name')
        teacher.middle_name=self.cleaned_data.get('Middle_Name')
        teacher.last_name=self.cleaned_data.get('Last_Name')
        teacher.mobile=self.cleaned_data.get('mobile')
        # teacher.dob=self.cleaned_data.get('dob')
        teacher.grade=self.cleaned_data.get('grade')
        teacher.school=self.cleaned_data.get('school')
        teacher.save()
        return teacher

class principalsignupform(UserCreationForm):
    email=forms.EmailField(required=True)
    First_Name=forms.CharField(required=True)
    Middle_Name=forms.CharField(required=False)
    Last_Name=forms.CharField(required=True)
    mobile=forms.CharField(required=True)
    school=forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model=User

    def __init__(self, *args, **kwargs):
        super(principalsignupform, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None
        self.label_suffix = ""

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_principal = True
        user.save()
        principal = user_profile_principal.objects.create(user=user)
        principal.first_name=self.cleaned_data.get('First_Name')
        principal.middle_name=self.cleaned_data.get('Middle_Name')
        principal.last_name=self.cleaned_data.get('Last_Name')
        principal.mobile=self.cleaned_data.get('mobile')
        principal.school=self.cleaned_data.get('school')
        principal.save()
        return principal

class schoolsignupform(UserCreationForm):
    email=forms.EmailField(required=True)
    School_Name=forms.CharField(required=True)
    phone=forms.CharField(required=True)
    mobile=forms.CharField(required=True)
    # established=forms.DateField(required=False)
    country=forms.CharField(required=True)
    state=forms.CharField(required=True)
    city=forms.CharField(required=True)
    street=forms.CharField(required=False)
    pin=forms.CharField(required=False)

    class Meta(UserCreationForm.Meta):
        model=User

    def __init__(self, *args, **kwargs):
        super(schoolsignupform, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None
        self.label_suffix = ""

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_school = True
        user.save()
        school = user_profile_school.objects.create(user=user)
        school.school_name=self.cleaned_data.get('School_Name')
        school.phone=self.cleaned_data.get('phone')
        school.mobile=self.cleaned_data.get('mobile')
        # school.established=self.cleaned_data.get('established')
        school.country=self.cleaned_data.get('country')
        school.state=self.cleaned_data.get('state')
        school.city=self.cleaned_data.get('city')
        school.street=self.cleaned_data.get('street')
        school.pin=self.cleaned_data.get('pin')
        school.save()
        return school

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )