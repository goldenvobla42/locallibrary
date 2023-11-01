from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Song, Author, Genre
from django.shortcuts import render
from .forms import SongSearchForm


def index(request):
    song_list = Song.objects.all()  # Retrieve all songs
    form = SongSearchForm(request.GET)  # Get the search form
    search_term = request.GET.get('search')  # Get the search term from the form data

    if search_term:
        # If a search term is provided, filter the songs based on the title
        song_list = song_list.filter(title__icontains=search_term)

    return render(request, 'index.html', {'song_list': song_list, 'form': form})


class SongListView(generic.ListView):
    model = Song
    paginate_by = 10

class SongDetailView(generic.DetailView):
    model = Song

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author


