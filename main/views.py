from django.shortcuts import render, get_object_or_404, redirect
from main.models import Project, Feedback


def index(request):
    return redirect('rsop')


def rsop(request):
    projects = Project.objects.all()
    return render(request, 'main/rsop.html', {'projects': projects})


def project(request, pk):
    p = get_object_or_404(Project, pk=pk)
    return render(request, 'main/project.html', {'project': p})


def project_feedback(request, pk):
    p = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        name = request.POST['name']
        content = request.POST['content']
        feedback = Feedback()
        feedback.name = name
        feedback.content = content
        feedback.project = p
        feedback.save()
        return redirect('rsop-projects', pk=pk)
    else:
        return render(request, 'main/project-feedback.html', {'project': p})

