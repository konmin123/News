from django import template
from django.db.models import Count

from News_Mod.models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('News_Api/list_categories.html')
def show_categories(kwarg1='Hello', kwarg2='user'):
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    return {'categories': categories, 'kwarg1': kwarg1, 'kwarg2': kwarg2}
