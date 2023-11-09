from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import ProjectForm

def projects(request):
    return render (request, 'projects/projects_list.html')


def project_new(request):
        form = ProjectForm()
        return render(request, 'projects/project_new.html', {
        'form': form
    })
