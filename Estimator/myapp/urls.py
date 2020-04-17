from django.urls import path
from myapp import views
from myapp.views import CountinentDetailView
app_name="myapp"


urlpatterns=[
path("home/<name>/",CountinentDetailView.as_view(),name="home"),
path("add/",views.AddFormView,name="add"),
path('',views.continentView,name="continent")
]
