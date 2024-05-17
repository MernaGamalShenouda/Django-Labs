from django.contrib import admin
from Books.models import Book
from Books.models import Category
from Books.models import ISBN

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'rate', 'views', 'user')
    list_filter = ('user', 'categories')
    search_fields = ('title', 'description')

admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(ISBN)