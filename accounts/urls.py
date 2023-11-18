from django.urls import path
from .views import SignUpView, ProfilPageView,AboutPageView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('myprofil/',ProfilPageView.as_view(),name='profil'),
    path('about/',AboutPageView.as_view(),name='about')
]