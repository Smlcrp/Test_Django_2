from django.shortcuts import render
from django.views import View 
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Artist

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

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


#class Song:
    #def __init__(self, name, img):
     #   self.name = name
      #  self.img = img


#songs = [
 #   Song('Song 1', 'https://online.berklee.edu/takenote/wp-content/uploads/2019/03/killerHooks-1920x1200.png'),
  #  Song('Song 2', 'https://27mi124bz6zg1hqy6n192jkb-wpengine.netdna-ssl.com/wp-content/uploads/2019/10/Our-Top-10-Songs-About-School-768x569.png'),
   # Song('Song 3', 'https://static01.nyt.com/images/2020/03/19/smarter-living/00well-handwashing-psa-music-notes/00well-handwashing-psa-music-notes-articleLarge-v3.gif?quality=75&auto=webp&disable=upscale'),
    #Song('Different Song', 'https://www.legalzoom.com/sites/lz.com/files/inline-images/xwoman-blue-dress-playing-blue-guitar.jpg.pagespeed.ic.oksHaDquuG.jpg'),
    #Song('Last Song', 'https://www.phoenixfm.com/wp-content/uploads/2019/10/song.png')
]

#class SongList(TemplateView):
 #   template_name = 'song_list.html'

  #  def get_context_data(self, **kwargs):
   #     context = super().get_context_data(**kwargs)
    #    context['songs'] = songs
     #   return context