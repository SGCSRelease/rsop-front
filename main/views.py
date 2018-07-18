from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from main.models import Project, Feedback


def index(request):
    return render(request, 'main/index.html')


def project(request, project_pk):
    p = get_object_or_404(Project, pk=project_pk)
    return render(request, 'main/project.html', {'project': p})


def project_feedback(request, project_pk):
    p = get_object_or_404(Project, pk=project_pk)
    if request.method == "POST":
        name = request.POST['name']
        content = request.POST['content']
        feedback = Feedback()
        feedback.name = name
        feedback.content = content
        feedback.project = p
        feedback.save()
        return HttpResponseRedirect(reverse('rsop-projects', kwargs={'project_pk': project_pk}))
    else:
        return render(request, 'main/project-feedback.html', {'project': p})

