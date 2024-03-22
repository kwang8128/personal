from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('database', views.database, name='database'),
  path('search', views.search, name='search'),
  path('modify', views.modify, name='modify'),
  path('create', views.create, name='create'),
  path('about', views.about, name='about'),
  path('text/<int:pk>', views.TextView.as_view(), name='text'),
  path('update', views.update, name='update'),
  path('text/<int:id>/delete', views.delete, name='delete'),
]