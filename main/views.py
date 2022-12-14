from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class VideosView(TemplateView):
    template_name = 'videos.html'


class DiscographyView(TemplateView):
    template_name = 'discography.html'


class ToursView(TemplateView):
    template_name = 'tours.html'


class BlogView(TemplateView):
    template_name = 'blog.html'
