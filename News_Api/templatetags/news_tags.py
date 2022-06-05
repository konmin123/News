from django import template

from News_Mod.models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('News_Api/list_categories.html')
def show_categories(kwarg1='Hello', kwarg2='user'):
    categories = Category.objects.all()
    return {'categories': categories, 'kwarg1': kwarg1, 'kwarg2': kwarg2}
