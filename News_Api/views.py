from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from News_Mod.models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
    model = News
    template_name = 'News_Api/public_news_list.html'
    context_object_name = "news"
    paginate_by = 5
    # extra_context = {'title': 'Главная'}
    # queryset = News.objects.select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(ListView):
    model = News
    template_name = 'News_Api/public_news_list.html'
    context_object_name = "news"
    allow_empty = False
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    template_name = 'News_Api/view_detail.html'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'News_Api/add_news.html'
    login_url = '/admin/'
    # success_url = reverse_lazy('home')
    # raise_exception = True


# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': "Список новостей",
#     }
#     return render(request, 'News_Api/index.html', context=context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'News_Api/category.html', {'news': news, 'category': category})


# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'News_Api/view_detail.html', {'news_item': news_item})

#
# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'News_Api/add_news.html', {'form': form})
