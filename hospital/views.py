from django.shortcuts import render,redirect,reverse
from django.conf import settings
from . import forms,models
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import DoctorRegisterForm,DoctorUpdateForm, AdminRegisterForm,AdminUpdateForm, PatientRegisterForm,PatientUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from hospital.models import Doctor,Admin,Patient
from django.contrib import auth
# Create your views here.
# Create your views here.
def dash_view(request):
    return render(request,'hospital/Patient/dashboard.html')
def bookapp_view(request):
    return render(request,'hospital/Patient/bookapp.html')
def calladoc_view(request):
    return render(request,'hospital/Patient/calladoc.html')
def feedback_view(request):
    return render(request,'hospital/Patient/feedback.html')
def feedback_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'hospital/Home/home.html')
    return render(request, 'hospital/Patient/feedback.html', {'form':sub})

def medicalreport_view(request):
    return render(request,'hospital/Patient/medicalreport.html')

def login_pat_view(request):
    if request.method=="POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('profile_pat.html')
        return render(request, 'hospital/Patient/login_pat.html', {'form': form})
    else: 
        form = AuthenticationForm()
                
    return render(request, 'hospital/Patient/login_pat.html', {'form': form})

def register_pat_view(request):
    if request.method=="POST":
        form = PatientRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            nu = User.objects.create_user(username=form.cleaned_data.get('username'),email=form.cleaned_data.get('email'),password=form.cleaned_data.get('password1'))
            doc = Patient(user=nu,firstname=form.cleaned_data.get('firstname'),
                        lastname=form.cleaned_data.get('lastname'),
                        age=form.cleaned_data.get('age'),
                        dob=form.cleaned_data.get('dob'),
                        address=form.cleaned_data.get('address'),
                        city=form.cleaned_data.get('city'),
                        country=form.cleaned_data.get('country'),
                        postalcode=form.cleaned_data.get('postalcode'),
                        image=request.FILES['image']
                        )
            doc.save()
            return redirect('login_pat.html')
        else:
            print(form.errors)
    else: 
        form = PatientRegisterForm()
    
    return render(request,'hospital/Patient/register_pat.html',{'form': form})

@login_required
def profile_pat_view(request):
    pat = Patient.objects.filter(user_id=request.user.id).first()
    #return render(request,'hospital/Doctor/profile_doc.html',{'doc':doc})
    if request.method=="POST":
        p_form = PatientUpdateForm(request.POST, request.FILES, instance=pat)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile_pat.html')
    else:
        p_form = PatientUpdateForm(instance=pat)
    context = {
        'p_form': p_form,
        'pat': pat
     }
    return render(request,'hospital/Patient/profile_pat.html',context)

def yourhealth_view(request):
    return render(request,'hospital/Patient/yourhealth.html')

def dash_doc_view(request):
    return render(request,'hospital/Doctor/dashboard_doc.html')
def bookapp_doc_view(request):
    return render(request,'hospital/Doctor/bookapp_doc.html')
def calladoc_doc_view(request):
    return render(request,'hospital/Doctor/calladoc_doc.html')
def feedback_doc_view(request):
    return render(request,'hospital/Doctor/feedback_doc.html')
def feedback_doc_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'hospital/Home/home.html')
    return render(request, 'hospital/Doctor/feedback_doc.html', {'form':sub})
def login_doc_view(request):
    if request.method=="POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('profile_doc.html')
        return render(request, 'hospital/Doctor/login_doc.html', {'form': form})
    else: 
        form = AuthenticationForm()
                
    return render(request, 'hospital/Doctor/login_doc.html', {'form': form})

def register_doc_view(request):
    if request.method=="POST":
        form = DoctorRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            nu = User.objects.create_user(username=form.cleaned_data.get('username'),email=form.cleaned_data.get('email'),password=form.cleaned_data.get('password1'))
            doc = Doctor(user=nu,firstname=form.cleaned_data.get('firstname'),
                        lastname=form.cleaned_data.get('lastname'),
                        age=form.cleaned_data.get('age'),
                        dob=form.cleaned_data.get('dob'),
                        address=form.cleaned_data.get('address'),
                        city=form.cleaned_data.get('city'),
                        country=form.cleaned_data.get('country'),
                        postalcode=form.cleaned_data.get('postalcode'),
                        image=request.FILES['image']
                        )
            doc.save()
            return redirect('login_doc.html')
        else:
            print(form.errors)
    else: 
        form = DoctorRegisterForm()
    
    return render(request,'hospital/Doctor/register_doc.html',{'form': form})



@login_required
def profile_doc_view(request):
    doc = Doctor.objects.filter(user_id=request.user.id).first()
    #return render(request,'hospital/Doctor/profile_doc.html',{'doc':doc})
    if request.method=="POST":
        p_form = DoctorUpdateForm(request.POST, request.FILES, instance=doc)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile_doc.html')
    else:
        p_form = DoctorUpdateForm(instance=doc)
    context = {
        'p_form': p_form,
        'doc': doc
     }
    return render(request,'hospital/Doctor/profile_doc.html',context)
    

def yourhealth_doc_view(request):
    return render(request,'hospital/Doctor/yourhealth_doc.html')

def medicalreport_doc_view(request):
    return render(request,'hospital/Doctor/medicalreport_doc.html')




def dash_adm_view(request):
    return render(request,'hospital/Admin/dashboard_adm.html')
def bookapp_adm_view(request):
    return render(request,'hospital/Admin/bookapp_adm.html')
def calladoc_adm_view(request):
    return render(request,'hospital/Admin/calladoc_adm.html')
def medicalreport_adm_view(request):
    return render(request,'hospital/Admin/medicalreport_adm.html')
def yourhealth_adm_view(request):
    return render(request,'hospital/Admin/yourhealth_adm.html')


def login_adm_view(request):
    if request.method=="POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('profile_adm.html')
        return render(request, 'hospital/Admin/login_adm.html', {'form': form})
    else: 
        form = AuthenticationForm()
                
    return render(request, 'hospital/Admin/login_adm.html', {'form': form})

def register_adm_view(request):
    if request.method=="POST":
        form = AdminRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            nu = User.objects.create_user(username=form.cleaned_data.get('username'),email=form.cleaned_data.get('email'),password=form.cleaned_data.get('password1'))
            adm = Admin(user=nu,firstname=form.cleaned_data.get('firstname'),
                        lastname=form.cleaned_data.get('lastname'),
                        age=form.cleaned_data.get('age'),
                        dob=form.cleaned_data.get('dob'),
                        address=form.cleaned_data.get('address'),
                        city=form.cleaned_data.get('city'),
                        country=form.cleaned_data.get('country'),
                        postalcode=form.cleaned_data.get('postalcode'),
                        image=request.FILES['image']
                        )
            adm.save()
            return redirect('login_adm.html')
        else:
            print(form.errors)
    else: 
        form = AdminRegisterForm()
    
    return render(request,'hospital/Admin/register_adm.html',{'form': form})



@login_required
def profile_adm_view(request):
    adm = Admin.objects.filter(user_id=request.user.id).first()
    #return render(request,'hospital/Doctor/profile_doc.html',{'doc':doc})
    if request.method=="POST":
        p_form = AdminUpdateForm(request.POST, request.FILES, instance=adm)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile_adm.html')
    else:
        p_form = AdminUpdateForm(instance=adm)
    context = {
        'p_form': p_form,
        'adm': adm
     }
    return render(request,'hospital/Admin/profile_adm.html',context)



def home_view(request):
    return render(request,'hospital/Home/home.html')
def signup_pat_view(request):
    return render(request,'hospital/Home/signup_pat.html')
def signup_doc_view(request):
    return render(request,'hospital/Home/signup_doc.html')
def signup_adm_view(request):
    return render(request,'hospital/Home/signup_adm.html')
#def services_view(request):
#    return render(request,'hospital/Home/services.html')
#def contactus_view(request):
#    return render(request,'hospital/Home/contactus.html')
#def news_view(request):
#    return render(request,'hospital/Home/news.html')
def login_view(request):
    return render(request,'hospital/Home/login.html')