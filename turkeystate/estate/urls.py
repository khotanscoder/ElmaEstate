from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about-us/', about, name='about'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('realestate/', RealEstate.as_view(), name='realstate'),
    path('projects/', Projects.as_view(), name='projects'),
    path('estate-detail <int:pk>/', EstateDetail.as_view(), name='estate-detail'),
    path('blog-post-details/', blog_post_detail, name='blog-post-details'),
    path('blog-posts/', blog_posts, name='blog-posts'),
#     path('fleet/', offers, name='fleet'),
#     path('team/', team, name='team'),
#     path('terms/', terms, name='terms'),
#     path('testimonials/', testimonials, name='testimonials'),
]
