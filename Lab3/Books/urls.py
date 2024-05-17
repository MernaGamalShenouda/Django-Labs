from django.urls import path
from Books import views
from django.contrib.auth import views as auth_views


app_name = 'Books'

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='books-index'),
    path('book_detail/<int:pk>', views.book_detail, name='book-deatil'),
    path('book_delete/<int:pk>', views.book_delete, name='book-delete'),
    path('book_update/<int:pk>', views.book_update, name='book-update'),
    path('create/', views.book_create, name='book_create'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
]