from django.urls import path
from Books import views

app_name = 'Books'

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='books-index'),
    path('book_detail/<int:book_id>', views.book_detail, name='book-deatil'),
    path('book_delete/<int:book_id>', views.book_delete, name='book-delete'),
    path('book_update/<int:book_id>', views.book_update, name='book-update'),
    path('create/', views.book_create, name='book_create'),
]