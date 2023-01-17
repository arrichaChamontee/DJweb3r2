from django.shortcuts import render,HttpResponse

# def productadd_home(request):
#     return HttpResponse("<H1>Hello</H1>")

def testbt(request):
    return render(request,'productapp/testbt.html')

# Create your views here.
