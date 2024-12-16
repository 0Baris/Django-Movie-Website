from django.shortcuts import render, get_object_or_404
from .models import Category, Movie


def home(request):
    
    search_query = request.GET.get('search', '')

    if search_query:
        filmler = Movie.objects.filter(film_adi__icontains=search_query,anasayfa=True)
    else:
        filmler = Movie.objects.filter(anasayfa=True)
    
    context = {
        "kategoriler": Category.objects.all,
        "filmler": filmler,
        "page": "home"
    }

    return render(request, 'index.html', context)


def movies(request):

    context = {
        "kategoriler": Category.objects.all,
        "filmler": Movie.objects.all,
        
    }


    return render(request, 'movies.html', context)


def movie_details(request, id):

    context = {
        "movie": Movie.objects.get(id=id),
        "page": "movie_details"
    }

    return render(request, 'details.html', context)


def category(request, id):
    kategori = get_object_or_404(Category, id=id)
    page = request.GET.get('page', 'home')
    if page == 'movies':
        filmler = Movie.objects.filter(category=kategori)
    else:
        filmler = Movie.objects.filter(category=kategori, anasayfa=True)
    context = {
        "kategoriler": Category.objects.all(),
        "kategori": kategori,
        "filmler": filmler,
        "page": page
    }
    return render(request, 'category.html', context)