from unicodedata import name
from django.urls import path
from .import views
# from .views import PostlListView


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.post_detail, name = 'details'),
    # path('blog/', PostlListView.as_view(), name='blog'),
    path('contact/', views.contact, name='contact')
]
