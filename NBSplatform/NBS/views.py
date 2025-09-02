from django.shortcuts import get_object_or_404, render
from .models import Project

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def projects_index(request):
    projects = Project.objects.all().order_by("name")
    return render(request, 'projects_index.html', {"projects": projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})

def articles_index(request):
    return render(request, 'articles_index.html')

def article_detail(request, article_id):
    return render(request, 'article_detail.html', {'article_id': article_id})

def about_page(request):
    return render(request, 'about_page.html')

def contact_page(request):
    return render(request, 'contact_page.html')

