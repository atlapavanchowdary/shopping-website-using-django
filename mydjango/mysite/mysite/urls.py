"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from garments.views import index,aboutus,formal_shirts,causual_shirts,t_shirts,trouser,jean,track_pant

urlpatterns = [
    url(r'^admin/', admin.site.urls), #admin pannel
    url(r'^$',index), #in the first page index will be displayed
    #index lst is converted into tuple so we use ,
    url(r'^aboutus$',aboutus),
    url(r'^formal_shirts$',formal_shirts),
    url(r'^causual_shirts$',causual_shirts),
    url(r'^t_shirts$',t_shirts),
    url(r'^trouser$',trouser),
    url(r'^jean$',jean),
    url(r'^track_pant$',track_pant),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #setting for media and url
