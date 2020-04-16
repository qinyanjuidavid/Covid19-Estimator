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
            #challenge 1
            currentlyInfected=reportedCases*10
            currentlyInfectedsevere=reportedCases*50
            time=period/3
            actualtime=2*round(time,0)
            InfectionByRequestedTime=currentlyInfected*actualtime
            InfectionByRequestedTimeSevere=currentlyInfectedsevere*actualtime
            #challenge 2
            severeCasesByRequestedTime_impact=InfectionByRequestedTime*0.15
            severeCasesByRequestedTime_severe=InfectionByRequestedTimeSevere*0.15


    else:
        form=Covid19Form()

    context={
    'form':form,
    'currentlyInfected':currentlyInfected,
    'currentlyInfectedsevere':currentlyInfectedsevere,
    'InfectionByRequestedTime':InfectionByRequestedTime,
    'InfectionByRequestedTimeSevere':InfectionByRequestedTimeSevere,
    'severeCasesByRequestedTime_impact':severeCasesByRequestedTime_impact,
    'severeCasesByRequestedTime_severe':severeCasesByRequestedTime_severe,
    }
    return render(request,'myapp/home.html',context)
