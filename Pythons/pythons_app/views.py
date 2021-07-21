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
        form = CreatePythonForm(request.POST)
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

#
# def create(request):
#     if request.method == "GET":
#         book = BookForm()
#         context = {
#             'book': book,
#         }
#         return render(request, 'create.html', context)
#     book = BookForm(request.POST)
#     if book.is_valid():
#         book.save()
#         return redirect('index')
#     return render(request, 'create.html')
#
#
# def update(request, pk):
#     book = Book.objects.get(pk=pk)
#     if request.method == "GET":
#         form = BookForm(instance=book)
#         context = {
#             'book': form,
#         }
#         return render(request, 'create.html', context)
#     form = BookForm(
#         request.POST,
#         instance=book
#     )
#     if form.is_valid():
#         book = form.save()
#         book.save()
#         return redirect('index')
#     return render(request, 'edit.html')
