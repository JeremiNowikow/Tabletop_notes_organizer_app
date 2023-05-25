from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import UpdateView

from organizer.models import *


# Create your views here.

class MainPageView(View):
    def get(self, request):
        return render(request, 'organizer/main_page.html')

class CharacterListView(View):
    def get(self, request):
        characters = Character.objects.all().order_by('name')
        paginator = Paginator(characters, 25)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'organizer/characters.html', {'page_obj': page_obj})

    def post(self, request):
        if 'all-chars' in request.POST:
            characters = Character.objects.all().order_by('name')
        elif 'only-pcs' in request.POST:
            characters = PlayerCharacter.objects.all().order_by('name')
        elif 'only-npcs' in request.POST:
            characters = NonPlayableCharacter.objects.all().order_by('name')
        elif 'search' in request.POST:
            search = request.POST.get('searchText')
            characters = Character.objects.filter(name__icontains=search).order_by('name')
        paginator = Paginator(characters, 25)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'organizer/characters.html', {'page_obj': page_obj})


