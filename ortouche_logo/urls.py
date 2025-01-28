from django.urls import path
from. import views

app_name = 'ortouche_logo'

urlpatterns = [
    path('logo/',views.logo,name="logo"),
]
