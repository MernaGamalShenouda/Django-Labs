from django.shortcuts import render, redirect

# Create your views here.

books_list = [
    {
        'index': 0,
        'id': 1,
        'title': 'The Catcher in the Rye',
        'author': 'J.D. Salinger',
        'genre': 'Fiction',
        'description': "The story of Holden Caulfield, a young man who has been expelled from prep school. Through his first-person narration, Holden reveals his inner thoughts and feelings about life, society, and his own experiences.",
    },
    {
        'index': 1,
        'id': 2,
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'genre': 'Fiction',
        'description': "Set in the 1930s in the fictional town of Maycomb, Alabama, the story follows the trial of a black man, Tom Robinson, who is falsely accused of raping a white woman. Through the eyes of Scout Finch, the daughter of the defense attorney, the novel explores themes of racism, justice, and morality.",
    },
    {
        'index': 2,
        'id': 3,
        'title': '1984',
        'author': 'George Orwell',
        'genre': 'Science Fiction',
        'description': "A dystopian novel set in a totalitarian society ruled by the Party led by Big Brother. The protagonist, Winston Smith, works for the Party and becomes disillusioned with its oppressive regime. As he rebels against the Party's control and falls in love, he risks everything to seek freedom and truth.",
    },
    {
        'index': 3,
        'id': 4,
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'genre': 'Classic Literature',
        'description': "A romantic novel set in early 19th-century England, it follows the emotional development of Elizabeth Bennet, the protagonist, who learns the error of making hasty judgments and comes to appreciate the difference between superficial goodness and actual goodness.",
    },
    {
        'index': 4,
        'id': 5,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'genre': 'Fiction',
        'description': "Set in the summer of 1922, the novel portrays the Jazz Age and explores themes of decadence, idealism, resistance to change, and social upheaval. The story follows the mysterious Jay Gatsby, who throws extravagant parties in hopes of rekindling his romance with Daisy Buchanan, a married woman.",
    },
    {
        'index': 5,
        'id': 6,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J.K. Rowling',
        'genre': 'Fantasy',
        'description': "The first book in the Harry Potter series, it follows the journey of a young wizard, Harry Potter, who discovers his magical heritage on his eleventh birthday when he receives a letter of acceptance to Hogwarts School of Witchcraft and Wizardry.",
    },
    {
        'index': 6,
        'id': 7,
        'title': 'The Hobbit',
        'author': 'J.R.R. Tolkien',
        'genre': 'Fantasy',
        'description': "The prelude to Tolkien's epic fantasy trilogy, The Lord of the Rings, it follows the journey of Bilbo Baggins, a hobbit who is enlisted by the wizard Gandalf to accompany a group of dwarves on a quest to reclaim their homeland from the dragon Smaug.",
    },
    {
        'index': 7,
        'id': 8,
        'title': 'The Chronicles of Narnia: The Lion, the Witch and the Wardrobe',
        'author': 'C.S. Lewis',
        'genre': 'Fantasy',
        'description': "The first book in The Chronicles of Narnia series, it tells the story of four siblings—Peter, Susan, Edmund, and Lucy Pevensie—who are evacuated from London during World War II and discover the magical land of Narnia through a wardrobe in the country home where they are staying.",
    },
    {
        'index': 8,
        'id': 9,
        'title': 'Moby-Dick',
        'author': 'Herman Melville',
        'genre': 'Adventure',
        'description': "A novel that tells the story of the obsessive quest of Captain Ahab, who seeks revenge on the giant white sperm whale Moby Dick, which had previously bitten off Ahab's leg at the knee during a whaling voyage.",
    },
    {
        'index': 9,
        'id': 10,
        'title': 'The Lord of the Rings: The Fellowship of the Ring',
        'author': 'J.R.R. Tolkien',
        'genre': 'Fantasy',
        'description': "The first volume in Tolkien's epic fantasy trilogy, it follows the journey of Frodo Baggins, a hobbit who inherits the One Ring and must journey across Middle-earth to destroy it in the fires of Mount Doom, accompanied by a fellowship of companions.",
    },
]

def home(request):
    return render(request, 'Books/welcome.html')

def index(request):
    my_context = {
        'books_list': books_list
    }
    return render(request, 'Books/books_list.html', context=my_context)

def _get_book(book_id):
    for book in books_list:
        if 'id' in book and book['id'] == book_id:
            return book
    return None

def book_detail(request, *args, **kwrgs):
   book_id = kwrgs.get('book_id')
   book_object = _get_book(book_id)
   my_context = {
       'book_id': book_object.get('id'),
       'book_title': book_object.get('title'),
       'book_author': book_object.get('author'),
       'book_genre': book_object.get('genre'),
       'book_description': book_object.get('description') 
   }
   return render(request, 'Books/book_details.html', context=my_context)

def book_delete(request, **kwrgs):
    book_id = kwrgs.get('book_id')
    book_object = _get_book(book_id)
    if book_object:
        books_list.remove(book_object)
    return redirect("Books:books-index")

def book_update(request, book_id):
    book_object = None
    for book in books_list:
        if book['id'] == book_id:
            book_object = book
            break

    if book_object is None:
        return redirect('Books:books-index')  

    if request.method == 'POST':
        book_object['title'] = request.POST.get('title')
        book_object['author'] = request.POST.get('author')
        book_object['genre'] = request.POST.get('genre')
        book_object['description'] = request.POST.get('description')
        return redirect('Books:books-index')  

    return render(request, 'Books/book_update.html', {'book_object': book_object})

def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        description = request.POST.get('description')
        new_book = {'id': len(books_list) + 1, 'title': title, 'author': author,'genre':genre, 'description': description}
        books_list.append(new_book)
        return redirect('Books:books-index')  

    return render(request, 'Books/book_create.html')