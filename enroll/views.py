from django.shortcuts import render

# Create your views here.
# def home(request):
#     return render(request, 'enroll/base.html')

def add_show(request):
    return render(request,'enroll/addandshow.html')