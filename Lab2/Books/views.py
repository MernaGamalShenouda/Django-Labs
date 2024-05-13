from django.shortcuts import render, redirect
from Books.models import Book
from .forms import BookForm

def home(request):
    return render(request, 'Books/welcome.html')

def index(request):
    books_list =  Book.objects.all()
    return render(request, 'Books/books_list.html', context={'books_list': books_list})

def book_detail(request, pk):
   book = Book.objects.get(pk=pk)
   return render(request, 'Books/book_details.html', context={'book': book})

def book_delete(request, pk):    
    Book.objects.get(pk=pk).delete()
    return redirect("Books:books-index")

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Books:books-index')
    else:
        form = BookForm()

    return render(request, 'Books/book_create.html', {'form': form})

def book_update(request, pk):
    try:
        book_object = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return redirect('Books:books-index')  

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book_object)
        if form.is_valid():
            form.save()
            return redirect('Books:books-index')
    else:
        form = BookForm(instance=book_object)

    return render(request, 'Books/book_update.html', {'form': form})