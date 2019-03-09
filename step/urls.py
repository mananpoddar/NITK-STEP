from django.conf.urls import url
from step import views
from django.urls import path
app_name = "step"

urlpatterns = [
    url(r'^$', views.frontPage, name='front_page'),
    path('govprojects/', views.gov_projects, name='gov_projects'),
    path('ongoingprojects/', views.ongoing, name='ongoing'),
    path('comingevents/', views.comingevents, name='comingevents'),
]