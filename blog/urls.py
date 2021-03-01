from django.urls import path
import jobs.views
from . import views

urlpatterns = [
    path('',views.blogs,name="blogs"),  
    path('<int:blog_id>/',views.detail,name = "detail"),
] 
