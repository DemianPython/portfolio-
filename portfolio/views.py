from django.shortcuts import render
from portfolioapp.models import Project

def index(request):
    project = Project.objects.all()
    context = {'project':project}
    return render(request, 'index.html', context=context)

