"""
URL configuration for FirstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from FirstApp import views
from MultiViewsApp import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',views.display),
    path("welcome2/",views.show),
    path('hello/',views.hello),
    path('dtime/',views.senddatetime),
    #MultiViewsApp as v1(alias to views.py)
	path('mrng/',v1.f1),
	path('aftr/',v1.f2),
	path('evng/',v1.f3),
    
    #default-homepage-view
    re_path("^.*$",views.homepage),
]
