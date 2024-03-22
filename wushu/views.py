from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.db.models import Q

from .models import Text

# Create your views here.

def index(request):
  return render(request, 'index.html')

def database(request):
  context = {"texts": Text.objects.filter(action = "P")}
  return render(request, 'database.html', context)

# class DatabaseView(generic.ListView):
#   model = Text
#   context_object_name = "texts"
#   template_name = "database.html"
  
def search(request):
  query = request.GET.get('q')
  context = {"texts": Text.objects.filter(Q(art__icontains = query) | Q(title__icontains = query) | Q(subtype__icontains = query)).values()}
  return render(request, 'database.html', context)

class TextView(generic.DetailView):
  model = Text
  template_name = "text.html"

def modify(request):
  return render(request, 'modify.html')

def create(request):
  art = request.POST.get('art')
  subtype = request.POST.get('subtype')
  title = request.POST.get('title')
  link = request.POST.get('link')
  desc = request.POST.get('desc')
  text = Text(art=art, subtype=subtype, title=title, link=link, desc=desc, action='C')
  text.save()
  return database(request)

def update(request):
  art = request.POST.get('art')
  subtype = request.POST.get('subtype')
  title = request.POST.get('title')
  link = request.POST.get('link')
  desc = request.POST.get('desc')
  text = Text(art=art, subtype=subtype, title=title, link=link, desc=desc, action='U')
  text.save()
  return database(request)

def delete(request, id):
  text_to_delete = Text.objects.get(id=id)
  art = text_to_delete.art
  subtype = text_to_delete.subtype
  title = text_to_delete.title
  link = text_to_delete.link
  desc = text_to_delete.desc
  text = Text(art=art, subtype=subtype, title=title, link=link, desc=desc, action='D')
  text.save()
  return database(request)

def about(request):
  return render(request, 'about.html')

