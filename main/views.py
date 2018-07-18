from django.shortcuts import render, get_object_or_404
from main.models import Project, Feedback


def index(request):
    return render(request, 'main/index.html')


def project(request, project_pk):
    p = get_object_or_404(Project, pk=project_pk)
    return render(request, 'main/project.html', {'project': p })
