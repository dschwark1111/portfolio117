from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import ProjectForm
from .models import Project

def projects_list(request):
    projects = Project.objects.all()
    return render (request, 'projects/projects_list.html', {'projects' : projects})


def project_new(request):
        if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES)
            if form.is_valid():
                project = form.save()
                return redirect('projects_list')
        else:
            form = ProjectForm()

        return render(request, 'projects/project_new.html', {
        'form': form
    })
