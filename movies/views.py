from django.shortcuts import render, get_object_or_404
from .models import Category, Movie

## Test veritabanı
# kategoriler = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Horror"]
# filmler = [
#     {
#         "id": 1,
#         "film_adi": "Encanto",
#         "aciklama": "Disney",
#         "resim": "encanto.jpeg",
#         "anasayfa": True
#     },
#     {
#         "id": 2,
#         "film_adi": "Moana 2",
#         "aciklama": "Disney",
#         "resim": "moana2.jpeg",
#         "anasayfa": True

#     },
#     {
#         "id": 3,
#         "film_adi": "Thunderbolts",
#         "aciklama": "MARVEL",
#         "resim": "thunderbolts.jpg",
#         "anasayfa": False
#     },
#     {
#         "id": 4,
#         "film_adi": "US",
#         "aciklama": "Netflix",
#         "resim": "us.jpg",
#         "anasayfa": True
#     }
#     ]
# # Create your views here.

def home(request):
    
    context = {
        "kategoriler": Category.objects.all,
        "filmler": Movie.objects.filter(anasayfa=True),
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

