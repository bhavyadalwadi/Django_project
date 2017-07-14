from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic import View
from .models import Album
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form': form})
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns user object when credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})

''' this is bullshit instead of this functions create generic views as above  
#from django.http import Http404  #no need if you are usinf get_object_or_404
from django.shortcuts import render, get_object_or_404
from .models import Album, Song       #have to import it because we want to create link of the album


def index(request):
    all_albums = Album.objects.all()
    #context = {'all_albums': all_albums}        #info templet nees in order to work (Dictionaery)
    #return render(request, 'music/index.html', context)     # if you are using variable only once you should use direct value of it Eg.context you can comment/delete it now the variable
    return render(request, 'music/index.html', {'all_albums': all_albums})
def detail(request, album_id):
    #return HttpResponse("<h2>Details For Album Id:"+str(album_id)+"</h2>")      # what if fwe dont have that song user is requesting for or id is not valid, dont return this
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})
def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:                                #if they dont select song or try to hack
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "No song Selected..",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})
''' #try:                                    #there is a shortcut for this try method get_object_or_404 import with rander importation
    #    album = Album.objects.get(pk=album_id)
    #except Album.DoesNotExist:
    #    raise Http404("Album Does not Exist")
    #return render(request, 'music/detail.html', {'album': album})

'''if you want to clean up code lil bit and combine Loader and render ther is another way, its above code
from django.http import HttpResponse
from django.template import loader
from .models import Album       #have to import it because we want to create link of the album


def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    return HttpResponse(template.render(context, request))


def detail(request, album_id):
    return HttpResponse("<h2>Details For Album Id:"+str(album_id)+"</h2>")'''

'''this is the basif cunstruction but if you dont want to mix html code with python you use templets after importing thhem as shown above
from django.http import HttpResponse
from .models import Album       #have to import it because we want to create link of the album


def index(request):
    all_albums = Album.objects.all()
    html = ''
    for album in all_albums:            #this for loop is for Creating links of the Album
        url = '/music/' + str(album.id) + '/'
        html += '<a href= "' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)


def detail(request, album_id):
    return HttpResponse("<h2>Details For Album Id:"+str(album_id)+"</h2>")
'''