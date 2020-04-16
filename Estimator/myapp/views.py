from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myapp.forms import Covid19Form


def Home(request):
    if request.method=="POST":
        form=Covid19Form(request.POST or None,request.FILES or None)
        if form.is_valid():
            name=form.cleaned_data['name']
            avgAge=form.cleaned_data['avgAge']
            avgDailyIncomeInUsd=form.cleaned_data['avgDailyIncomeInUsd']
            avgDailyIncomePopulation=form.cleaned_data['avgDailyIncomePopulation']
            period=form.cleaned_data['period']
            timeToElapse=form.cleaned_data['timeToElapse']
            population=form.cleaned_data['population']
            totalHospitalBeds=form.cleaned_data['totalHospitalBeds']
    else:
        form=Covid19Form()

    context={
    'form':form
    }
    return render(request,'myapp/home.html',context)
