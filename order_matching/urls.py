from django.urls import path
from . import views

app_name='order_matching'

urlpatterns=[path("", views.landing_page, name="landing-page")]