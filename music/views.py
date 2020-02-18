from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View 

from .models import Album
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = "music/index.html"
    context_object_name= 'all_albums'

    def get_queryset(self):   
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name='music/detail.html'


class AlbumCreate(CreateView):
    model= Album
    fields=['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model= Album
    fields=['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model=Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class=UserForm
    template_name = '/music/registration_form.html'

# Display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
        
        # cleaned (nomalized) Data
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # in database password is hash, need to hash and save
        user.set_password(password)
        user.save()
        



















# from django.shortcuts import render, get_object_or_404

# from django.http import Http404
# from django.http import HttpResponse
# from django.template import loader
# from .models import Album,Song

# Create your views here.

#  def index(request):
#     all_albums = Album.objects.all()
#     context = {'all_albums': all_albums}
#     return render(request,'music/index.html',context)

# def detail(request,album_id):
#     # try:
#     #     album =Album.objects.get(pk=album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("Album does not exist")
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request,'music/detail.html',{'album': album})

# def favorite(request,album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except(KeyError, Song.DoesNotExist):
#         return render(request,'music/detail.html',{
#             'album': album,
#            'error_message': 'You did not select a valid song'
#         })
#     else:
#         selected_song.is_favorite = True
#         selected_song.save()
#         return render(request,'music/detail.html',{'album': album})

