from django.contrib import admin
from django.urls import path
from StudentApp import views

urlpatterns = [
    # student/ <--- is for POST and GET methods
    path('student/',views.studentApi),

    # student/<int:pk> <--- is for PUT and DELETE methods    
    path('student/<int:id>',views.studentApi),
    path('admin/', admin.site.urls),
]