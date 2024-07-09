from articles.models import Article
from django.shortcuts import render


    
def home_view(request, *args, **kwargs):
    Article_obj = Article.objects.get(id=1)
    obj_queryset = Article.objects. all()
    context = {
        'Article_obj': Article_obj,
        'obj_queryset': obj_queryset,
        'title':  Article_obj.title,
        'content': Article_obj.content,
        'id': Article_obj.id
    }
    return render(request, 'home.html', context=context)

