from django.shortcuts import render, HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse("<H1>Hello World, This is my First Web </H1>"
                        "<H2>I Love Girls' Generation, It's My Life</H2>")

def firstPage(request):
    return render(request, 'FirstPage.html')

def secondpage(request):
    return render(request, 'SecondPage.html')

def thirdpage(request):
    return render(request, 'Thirdpage.html')

def hnypage(request):
    return render(request, 'hnpPage.html')

def home(request):
    return  render(request,'home.html')