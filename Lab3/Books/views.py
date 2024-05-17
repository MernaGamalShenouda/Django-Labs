from django.shortcuts import render, redirect
from Books.models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'Books/welcome.html')

@login_required(login_url='/login')
def index(request):
    books_list =  Book.objects.all()
    return render(request, 'Books/books_list.html', context={'books_list': books_list})

@login_required(login_url='/login')
def book_detail(request, pk):
   book = Book.objects.get(pk=pk)
   return render(request, 'Books/book_details.html', context={'book': book})

@login_required(login_url='/login')
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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Books:login')
    else:
        form = UserCreationForm()
    return render(request, 'Books/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Books:home')
    return render(request, 'Books/login.html')

def logout_view(request):
    logout(request)
    return redirect('Books:login')