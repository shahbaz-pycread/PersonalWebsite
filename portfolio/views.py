from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'portfolio/index.htm')

def contact(request):
    return render(request,'portfolio/contact.htm')
