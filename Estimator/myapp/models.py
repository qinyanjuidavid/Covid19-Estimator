from django.db import models

class Covid19(models.Model):
    continent=(
    ('Africa','Africa'),
    ('Antarctica','Antarctica'),
    ('Asia','Asia'),
    ("Australia",'Australia'),
    ('Europe','Europe'),
    ('North America','North America'),
    ('South America','South America'),
    )
    name=models.CharField(max_length=15,choices=continent,verbose_name="Continent",unique=True)
    avgAge=models.FloatField(verbose_name="Average Age")
    avgDailyIncomeInUsd=models.FloatField(verbose_name="Average Income In USD",default=1.5)
    avgDailyIncomePopulation=models.FloatField(verbose_name="Average Daily Income Population",default=0.65)
    period=models.FloatField(verbose_name="days")
    timeToElapse=models.FloatField(verbose_name="Time To Elapse",blank=True,null=True)
    reportedCases=models.FloatField(verbose_name="reported_cases")
    population=models.FloatField(verbose_name='Population')
    totalHospitalBeds=models.FloatField(verbose_name="Total Hospital Beds")

    def __str__(self):
        return self.name
class Impact(models.Model):
    name=models.CharField(max_length=15,unique=True)
    currentlyInfected=models.FloatField(verbose_name="Currently Infected")
    InfectionByRequestedTime=models.FloatField(verbose_name="Infections By Requested Time")
    severeCasesByRequestedTime_impact=models.FloatField(verbose_name="Severe Cases By Requested Time")
    hospitalBedsByRequestedTime_impact=models.FloatField(verbose_name="Hospital Beds")
    casesForICUByRequestedTime_impact=models.FloatField(verbose_name='Cases For ICU')
    casesForVentilatorsByRequestedTime_impact=models.FloatField(verbose_name="Cases For Ventilators")
    dollarsInFlight_impact=models.FloatField(verbose_name="Dollars In Flight")

    def __str__(self):
        return self.name
class SevereImpact(models.Model):
    name=models.CharField(max_length=15,verbose_name="Continent")
    currentlyInfectedsevere=models.FloatField(verbose_name="Currently Infected")
    InfectionByRequestedTimeSevere=models.FloatField(verbose_name="Infections By Requested Time")
    severeCasesByRequestedTime_severe=models.FloatField(verbose_name="Severe Cases By Requested Time")
    hospitalBedsByRequestedTime_severe=models.FloatField(verbose_name="Hospital Beds")
    casesForICUByRequestedTime_severe=models.FloatField(verbose_name="Cases For ICU")
    casesForVentilatorsByRequestedTime_severe=models.FloatField(verbose_name="Cases For Ventilators")
    dollarsInFlight_severe=models.FloatField(verbose_name="Dollars In Flight")

    def __str__(self):
        return self.name
