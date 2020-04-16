from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect


def Home(request):
    context={

    }
    return render(request,'myapp/home.html',context)
