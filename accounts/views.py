from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfilPageView(TemplateView):
    template_name = 'profil.html'   

class AboutPageView(TemplateView):
    template_name = 'about.html'      