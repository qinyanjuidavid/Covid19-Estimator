from django.urls import path
from myapp import views
app_name="myapp"


urlpatterns=[
path("home/<id>/",views.Home,name="home"),
path("add,",views.AddFormView,name="add"),
path('',views.continentView,name="continent")
]
