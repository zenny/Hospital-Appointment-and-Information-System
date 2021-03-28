from django import forms
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Doctor,Admin,Patient
#from .models import Doctor


class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30,label="",widget=forms.TextInput(attrs={'placeholder': 'NAME'}))
    Name.widget.attrs.update({'class' : 'app-form-control'})
    Email = forms.EmailField(label="",widget=forms.TextInput(attrs={'placeholder': 'EMAIL'}))
    Email.widget.attrs.update({'class' : 'app-form-control'})
    Message = forms.CharField(max_length=500,label="",widget=forms.TextInput(attrs={'placeholder': 'MESSAGE'}))
    Message.widget.attrs.update({'class' : 'app-form-control'})

class DoctorRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField()
    lastname = forms.CharField()
    age = forms.IntegerField()
    dob = forms.DateField()
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postalcode = forms.IntegerField()
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'image', 'password1', 'password2']
        #fields = ['username', 'email', 'firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'password1', 'password2']


class DoctorUpdateForm(forms.ModelForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    age = forms.IntegerField()
    dob = forms.DateField()
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postalcode = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Doctor
        fields = ['firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'image']


class AdminRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField()
    lastname = forms.CharField()
    age = forms.IntegerField()
    dob = forms.DateField()
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postalcode = forms.IntegerField()
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'image', 'password1', 'password2']
        #fields = ['username', 'email', 'firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'password1', 'password2']


class AdminUpdateForm(forms.ModelForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    age = forms.IntegerField()
    dob = forms.DateField()
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postalcode = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Admin
        fields = ['firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'image']


class PatientRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField()
    lastname = forms.CharField()
    age = forms.IntegerField()
    dob = forms.DateField()
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postalcode = forms.IntegerField()
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'image', 'password1', 'password2']
        #fields = ['username', 'email', 'firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'password1', 'password2']


class PatientUpdateForm(forms.ModelForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    age = forms.IntegerField()
    dob = forms.DateField()
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postalcode = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Patient
        fields = ['firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'image']
