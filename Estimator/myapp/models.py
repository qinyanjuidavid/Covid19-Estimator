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
    name=models.CharField(max_length=15,choices=continent)
    avgAge=models.IntegerField()
    avgDailyIncomeInUsd=models.IntegerField(default=1.5)
    avgDailyIncomePopulation=models.IntegerField(default=0.17)
    period=models.IntegerField(verbose_name="days")
    timeToElapse=models.IntegerField()
    reportedCases=models.IntegerField(verbose_name="reported_cases")
    population=models.IntegerField(verbose_name='Population')
    totalHospitalBeds=models.IntegerField(verbose_name="Total Hospital Beds")

    def __str__(self):
        return self.name
