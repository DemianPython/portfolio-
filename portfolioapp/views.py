from django.shortcuts import render
from .models import Project


def see_portfolio(request):
    project = Project.objects.all()
    context = {'project':project}
    return render(request, 'portfolio/portfolio.html', context=context)

