from django.urls import path
from . import views


urlpatterns = [
   path('', views.accueil, name="accueil"),   
   path('blog-detail/<slug>', views.blog_detail , name="blog_detail"),
   path('see-blog/' , views.see_blog , name="see_blog"),
   path('brouillon/' , views.draft , name="draft"),
   path('all_pub/' , views.all_pub , name="all_pub"),
   
   path('about',views.about, name='about'),
    path('articles',views.articles, name='articles'),
    path('contact',views.contact, name='contact'),
    path('programme',views.programme, name='programme'),
    path('service',views.service, name='service'),
    path('team',views.team, name='team'),
    path('testimonial',views.testimonial, name='testimonial'),
    path('error',views.error, name='404'),
]

