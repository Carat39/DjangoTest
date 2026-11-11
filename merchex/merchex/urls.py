"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from listings import views

urlpatterns = [
    path('', views.home, name='home'),

    path('admin/', admin.site.urls), #On peut pas le name sinon ReverseMatch Error
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:band_id>/',views.band_detail, name='band-detail'),
    path('bands/add/',views.band_add, name='band-add'),
    path('bands/<int:band_id>/modify',views.band_modify, name='band-modify'),
    path('bands/<int:band_id>/delete',views.band_delete, name='band-delete'),
    

    path('about-us/', views.about, name='about-us'),

    path('listings/', views.listing_list,name='listing-list'),
    path('listings/<int:listing_id>', views.listing_detail, name='listing-detail'),
    path('listings/add/',views.listing_add, name='listing-add'),
    path('listings/<int:listing_id>/modify',views.listing_modify, name='listing-modify'),
    path('listings/<int:listing_id>/delete',views.listing_delete, name='listing-delete'),

    path('contact-us/', views.contact, name='contact-us'),
    path('email-sent', views.email_sent, name='email-sent')
    #path('profil/',views.mon_profil)
    #path('profil/<str:username>/', views.voir_profil_utilisateur, name='voir_profil_utilisateur')
]
