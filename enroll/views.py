from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
# def home(request):
#     return render(request, 'enroll/base.html')

def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            eml = fm.cleaned_data['email']
            pswd = fm.cleaned_data['password']
            reg = User(name=nm,email=eml,password=pswd)
            reg.save()

    else:
        fm = StudentRegistration()
    return render(request,'enroll/addandshow.html',{'form':fm})