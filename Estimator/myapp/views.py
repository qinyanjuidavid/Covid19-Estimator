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
            hospitalBedsByRequestedTime_impact=(totalHospitalBeds*0.35)-severeCasesByRequestedTime_impact
            hospitalBedsByRequestedTime_severe=(totalHospitalBeds*0.35)-severeCasesByRequestedTime_severe
            #challenge 3
            casesForICUByRequestedTime_impact=InfectionByRequestedTime*0.05
            casesForICUByRequestedTime_severe=InfectionByRequestedTimeSevere*0.05
            casesForVentilatorsByRequestedTime_impact=InfectionByRequestedTime*0.02
            casesForVentilatorsByRequestedTime_severe=InfectionByRequestedTimeSevere*0.02
            dollarsInFlight_impact=InfectionByRequestedTime*avgDailyIncomeInUsd*avgDailyIncomePopulation*30
            dollarsInFlight_impact=round(dollarsInFlight_impact,2)
            dollarsInFlight_severe=InfectionByRequestedTimeSevere*avgDailyIncomeInUsd*avgDailyIncomePopulation*30
            dollarsInFlight_severe=round(dollarsInFlight_severe,2)

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
    'hospitalBedsByRequestedTime_impact':hospitalBedsByRequestedTime_impact,
    'hospitalBedsByRequestedTime_severe':hospitalBedsByRequestedTime_severe,
    'casesForICUByRequestedTime_impact':casesForICUByRequestedTime_impact,
    'casesForICUByRequestedTime_severe':casesForICUByRequestedTime_severe,
    'casesForVentilatorsByRequestedTime_impact':casesForVentilatorsByRequestedTime_impact,
    'casesForVentilatorsByRequestedTime_severe':casesForVentilatorsByRequestedTime_severe,
    'dollarsInFlight_impact':dollarsInFlight_impact,
    'dollarsInFlight_severe':dollarsInFlight_severe
    }
    return render(request,'myapp/home.html',context)
