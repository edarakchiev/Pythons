from django.shortcuts import render, redirect

from Pythons.pythons_app.forms import CreatePythonForm
from Pythons.pythons_app.models import Python


def index(request):
    pythons = Python.objects.all()
    context = {
        'pythons': pythons
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        form = CreatePythonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'create.html')
    else:
        form = CreatePythonForm()
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def details(request, pk):
    python = Python.objects.get(pk=pk)
    context = {
        'python':python,
    }
    return render(request, 'details.html', context)


def edit(request, pk):
    python = Python.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreatePythonForm(request.POST, request.FILES, instance=python)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreatePythonForm(instance=python)
    context = {
        'form': form
    }
    return render(request, 'edit.html', context)


def delete(request, pk):
    python = Python.objects.get(pk=pk)
    python.delete()
    return redirect('index')