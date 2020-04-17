from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from myapp.forms import Covid19Form
from myapp.models import Impact,SevereImpact,Covid19
from django.views.generic import DetailView

def continentView(request):
    covid=Covid19.objects.all()
    context={
    'covid':covid
    }
    return render(request,'myapp/continent.html',context)

def AddFormView(request):
    if request.method=="POST":
        form=Covid19Form(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form=Covid19Form()
    context={
    "form":form
    }
    return render(request,'myapp/add.html',context)

def Home(request):
    currentlyInfected=0
    currentlyInfectedsevere=0
    InfectionByRequestedTime=0
    InfectionByRequestedTimeSevere=0
    severeCasesByRequestedTime_impact=0
    severeCasesByRequestedTime_severe=0
    hospitalBedsByRequestedTime_impact=0
    hospitalBedsByRequestedTime_severe=0
    casesForVentilatorsByRequestedTime_impact=0
    casesForVentilatorsByRequestedTime_severe=0
    casesForICUByRequestedTime_impact=0
    casesForICUByRequestedTime_severe=0
    dollarsInFlight_impact=0
    dollarsInFlight_severe=0
    name=" "
    form=Covid19Form()
    if form.is_valid():
        reportedCases=form.cleaned_data['reportedCases']
        name=form.cleaned_data['name']
        avgAge=form.cleaned_data['avgAge']
        avgDailyIncomeInUsd=form.cleaned_data['avgDailyIncomeInUsd']
        avgDailyIncomePopulation=form.cleaned_data['avgDailyIncomePopulation']
        period=form.cleaned_data['period']
        timeToElapse=form.cleaned_data['timeToElapse']
        population=form.cleaned_data['population']
        totalHospitalBeds=form.cleaned_data['totalHospitalBeds']
        #challenge 1
        name=name
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
        #*************saving infor
        impact=Impact(
        name=name,
        currentlyInfected=currentlyInfected,
        InfectionByRequestedTime=InfectionByRequestedTime,
        severeCasesByRequestedTime_impact=severeCasesByRequestedTime_impact,
        hospitalBedsByRequestedTime_impact=hospitalBedsByRequestedTime_impact,
        casesForICUByRequestedTime_impact=casesForICUByRequestedTime_impact,
        casesForVentilatorsByRequestedTime_impact=casesForVentilatorsByRequestedTime_impact,
        dollarsInFlight_impact=dollarsInFlight_impact
        )

        severeimpact=SevereImpact(
        name=name,
        currentlyInfectedsevere=currentlyInfectedsevere,
        InfectionByRequestedTimeSevere=InfectionByRequestedTimeSevere,
        severeCasesByRequestedTime_severe=severeCasesByRequestedTime_severe,
        hospitalBedsByRequestedTime_severe=hospitalBedsByRequestedTime_severe,
        casesForICUByRequestedTime_severe=casesForICUByRequestedTime_severe,
        casesForVentilatorsByRequestedTime_severe=casesForVentilatorsByRequestedTime_severe,
        dollarsInFlight_severe=dollarsInFlight_severe
        )
        severeimpact.save()
        impact.save()


class CountinentDetailView(DetailView):
    template_name = "myapp/home.html"
    def get_object(self):
        impactObj=get_object_or_404(Impact,name__iexact=self.kwargs.get("name"))
        covidObj=get_object_or_404(Covid19,name__iexact=self.kwargs.get("name"))
        severeObj=get_object_or_404(SevereImpact,name__iexact=self.kwargs.get("name"))
        context={
        'impactObj':impactObj,
        'severeObj':severeObj,
        'covidObj':covidObj
        }
        return context
