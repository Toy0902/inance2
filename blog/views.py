from django.shortcuts import render

from blog.forms import EmailForm
from blog.models import Profil


def contact(request):
    form = EmailForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
    return render(request,"contact.html",context={})

def service(request):
    return render(request,"service.html",context={})
# Create your views here.
def index(request):
    profil = Profil.objects.all()[0]
    context ={
        "profil": profil
    }
    return render(request, "index.html", context=context)
def about(request):
    return render(request, "about.html", context={})

def index_detel(request,id):
    from blog.models import Profil
    rasmi = Profil.objects.all()
    context = {
        "profil": rasmi
    }
    return render(request,'detel.html',context=context)