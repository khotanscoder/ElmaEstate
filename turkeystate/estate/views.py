from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Estate, Project


class HomeView(ListView):
    model = Estate
    template_name = 'home.html'


class RealEstate(ListView):
    model = Estate
    template_name = 'realstate.html'


class Projects(ListView):
    model = Project
    template_name = 'projects.html'


class EstateDetail(DetailView):
    model = Estate
    template_name = 'realestate.html'


class ProjectDeteil(DetailView):
    model = Project
    template_name = 'projects.html'


def about(request):
    return render(request, 'about-us.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')


# def projects(request):
#     return render(request, 'projects.html')


def blog_posts(request):
    return render(request, 'blog-posts.html')


#
# def team(request):
#     return render(request, 'team.html')


# def testimonials(request):
#     return render(request, 'testimonials.html')


def terms(request):
    return render(request, 'terms.html')


def blog_post_detail(request):
    return render(request, 'blog-post-details.html')

# def offer(request):
#     return render(request, 'offer.html')
