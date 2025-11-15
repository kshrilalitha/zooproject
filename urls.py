"""
URL configuration for zoo project.

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
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.display_landing,name="Mysore Zoo"),
    path('tiger/',views.display_tiger,name="Tiger"),
    path('lion/',views.display_lion,name="Lion"),
    path('elephant/',views.display_elephant,name="Elephant"),
    path('bear/',views.display_bear,name="Polar Bear"),
    path('dolphin/',views.display_dolphin,name="Dolphin"),
    path('animals/',views.animal_data,name="Animals"),
    path('login/',views.login,name="login endpoint"),
    path('zoos/',views.zoo_data,name="Zoo"),
    path('booking/',views.book_ticket,name="Booking"),
    path("animal/", views.get_animals,name="Animals"),
    path("caretakers/", views.get_caretakers,name="caretaker"),
    path("donated_by/", views.get_donors,name="DonatedBy"),
    path("add_animal/", views.add_animal,name="Add Animal"),
    path("update_animal/", views.update_animal,name="update Animal"),
    path("delete_animal/", views.delete_animal,name="Delete Animal"),
    path("animals_view/", views.get_animals),
    path("caretakers_view/", views.get_caretakers),
    path("donors_view/", views.get_donors),

]

    

