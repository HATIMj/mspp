#tion views
from django.contrib import admin
from django.urls import path,include
from jojo import views
urlpatterns = [
    path('',views.home,name="Home" ),
    path('about',views.about,name="About"),
    path('services',views.services,name="Services"),
    path('products',views.products,name="Products"),
    path('login',views.Login,name="Login"),
    path('logout',views.Logout,name="Logout"),
    path('createnewaccount',views.cna,name="CreateNewAccount")

]
]
