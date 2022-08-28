from django.shortcuts import render
from .models import MovieData
from django.views.generic import ListView
from django.core.paginator import Paginator


# Create your views here.


def movie_list(request):
    movies =MovieData.objects.all()
    paginator = Paginator(movies,4)
    page = request.GET.get('page')
    movies_obj = paginator.get_page(page)
    
    
    return render(request,'newapp/movie_list.html',{'movies':movies_obj})


class MovieListView(ListView):
    model = MovieData
    paginate_by = 4
    template_name = 'food/movie_list.html'
    context_object_name = 'movies'
    

