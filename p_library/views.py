from django.http import HttpResponse
from django.template import loader
from p_library.models import Friend
from .models import Book

def collections(request):
    template = loader.get_template('library.html')
    friends = Friend.objects.all()
    data = {
        "friends": friends,
    }
    return HttpResponse(template.render(data, request))

def index(request):
    template = loader.get_template('base.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "My library", 
        "books": books}
    return HttpResponse(template.render(biblio_data, request))