from django.urls import path
from main.views import (
    IndexView,
    AboutView,
    ContactView,
    VideosView,
    DiscographyView,
    ToursView, BlogView,
)

app_name = "main"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('videos/', VideosView.as_view(), name='videos'),
    path('discography/', DiscographyView.as_view(), name='discography'),
    path('tours/', ToursView.as_view(), name='tours'),
    path('blog/', BlogView.as_view(), name='blog'),
]
