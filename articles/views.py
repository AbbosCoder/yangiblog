from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import DeleteView, UpdateView
from .models import Article
# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.auther==self.request.user
    
class ArticleDetailView( DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'summary', 'body', 'photo',)
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.auther==self.request.user

class ArticleCreateView( LoginRequiredMixin , CreateView ):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'summary', 'body', 'photo',)
    

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser
    

