from django.shortcuts import redirect, render,HttpResponseRedirect
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
            return redirect('addandshow')
    else:
        fm = StudentRegistration()
    stud = User.objects.all()    
    return render(request,'enroll/addandshow.html',{'form':fm, 'stu':stud})

def delete(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect('addandshow')


def update(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render (request,'enroll/update.html',{'form':fm})