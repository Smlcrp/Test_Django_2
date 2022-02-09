from django.shortcuts import redirect
from django.views import View 
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Artist, Song, Playlist

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlists'] = Playlist.objects.all()
        return context

class About(TemplateView):
    template_name = 'about.html'



class ArtistList(TemplateView):
    template_name = 'artist_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["artists"] = Artist.objects.filter(name__icontains=name)
            context['header'] = f"Searching for {name}"
        else:
            context["artists"] = Artist.objects.all()
            context['header'] = "Trending Artists"
        return context




class ArtistCreate(CreateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = 'artist_create.html'
    def get_success_url(self):
        return reverse('artist_detail', kwargs = {'pk': self.object.pk})



class ArtistDetail(DetailView):
    model = Artist
    template_name = 'artist_detail.html'



class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = 'artist_update.html'
    def get_success_url(self):
        return reverse('artist_detail', kwargs = {'pk': self.object.pk})



class ArtistDelete(DeleteView):
    model = Artist
    template_name = 'artist_delete_confirmation.html'
    success_url = '/artists/'




class SongCreate(View):
    def post(self, request, pk):
        title = request.POST.get('title')
        length = request.POST.get('length')
        artist = Artist.objects.get(pk=pk)
        Song.objects.create(title=title, length=length, artist=artist)
        return redirect('artist_detail', pk=pk)



class PlaylistSongAssoc(View):
    def get(self, request, pk, song_pk):
        assoc = request.GET.get('assoc')
        if assoc == 'remove':
            Playlist.objects.get(pk=pk).songs.remove(song_pk)
        if assoc == 'add':
            Playlist.objects.get(pk=pk).songs.add(song_pk)
        return redirect('home')