from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View,FormView
from .models import Playlist,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.urls import reverse_lazy,reverse



from django.contrib.auth.views import LoginView


# Create your views here.

class UserLogin(LoginView):
    model=Playlist
    redirect_authenticated_user = True
    template_name = 'base/login.html'
    def get_success_url(self):
        return reverse_lazy("home")

class Register(FormView):
    form_class =UserCreationForm
    template_name = 'base/register.html'
    redirect_authenticated_user=True
    success_url = reverse_lazy('create-profile')

    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(Register,self).form_valid(form)

#class UserProfile(DetailView):
#    model=Profile
#    context_object_name = 'profile'

class UserProfile(ListView):
    model = Profile
    context_object_name= "profile"
    template_name = "base/profile_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = context['profile'].filter(user=self.request.user)
        context['count'] = context['profile'].count()
        return context

class CreateProfile(CreateView):
    model=Profile
    fields='__all__'
    success_url= reverse_lazy('home')

class Songslist(ListView):
    model= Playlist
    context_object_name= "playlists"
    template_name = "base/Song_list.html"




class UserSongslist(ListView):
    model = Playlist
    context_object_name= "user_playlists"
    template_name = "base/usersongs_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_playlists'] = context['user_playlists'].filter(user=self.request.user)
        context['count'] = context['user_playlists'].count()
        return context

class PlaylistDetails(DetailView):
    model = Playlist
    context_object_name = "playlists"


class CreatePlaylist(CreateView):
    model=Playlist
    fields = "__all__"
    success_url = reverse_lazy("posted_playlist")

class UpdatePlaylist(UpdateView):
    model = Playlist
    fields = "__all__"
    success_url = reverse_lazy("posted_playlist")

class DeletePlaylist(DeleteView):
    model=Playlist
    context_object_name = "playlists"
    success_url = reverse_lazy("posted_playlist")


'''class AddPush(View):
    def playlist(self, request , pk ,*args ,**kwargs):
        playlist=Playlist.objects.get(pk=pk)
        pushed=False

        for push in playlist.likes.all():
            if push == request.user:
                pushed=True
                break

        if not pushed:
            playlist.likes.add(request.user)

        if pushed:
            playlist.likes.remove(request.user)

        a = request.POST.get('next','/')

        return HttpResponseRedirect(a)'''

def PushView(request,pk):
    post=get_object_or_404(Playlist ,id=request.POST.get('playlist_id'))
    post.push.add(request.user)
    return HttpResponseRedirect(reverse('home'))
