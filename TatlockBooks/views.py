from django.http import HttpResponse
from django.shortcuts import render_to_response
from BookExhibit.models import Book, Author, Publisher, Translator, Work

def home(request):
	authors = Author.objects.all().order_by('name')
	publishers = Publisher.objects.all().order_by('name')
	translators = Translator.objects.all().order_by('name')
	books = Book.objects.all().order_by('title')
	works = Work.objects.all().order_by('name')
	#pubyear
	#series = Series.objects.all().order_by('name')
	return render_to_response("Home.html",{'authors' : authors, 'publishers' : publishers, 'translators' : translators, 'books' : books, 'works' : works})
    
def welcome(request):
	return render_to_response("welcome.html")
	
def contact(request):
	return render_to_response("contact.html")
	
def about(request):
	return render_to_response("about.html")	
    
def bookpage(request, book_label):
	book = Book.objects.filter(label=book_label)[0]
	return render_to_response("book_template.html", {'book': book})

def workpage(request, work_id):
	work = Work.objects.filter(id = work_id)[0]
	translators = Translator.objects.filter(book__worklink = work)
	publishers = Publisher.objects.filter(book__worklink = work)
	#editions = Book.objects.filter(worklink = work)
	return render_to_response("work_template.html", {'work' : work, 'author': author, 'translators':translators, 'publishers':publishers})

#def seriespage(request, series_id):
#	series = Series.objects.filter(id = series_id)[0]
#	creator = Publisher.objects.filter(book__serieslink = series)
#	books = Book.objects.filter(book__serieslink = series)	
	 
def authorpage(request, author_id):
	author = Author.objects.filter(id = author_id)[0]
	publishers = Publisher.objects.filter(book__authorlink = author)
	translators = Translator.objects.filter(book__authorlink = author)
	works = Work.objects.filter(book__authorlink = author)
    # series = Series.objects
	return render_to_response("author_template.html", {'author' : author, 'publishers' : publishers, 'translators' : translators, 'works' : works})

def translatorpage(request, translator_id):
	translator = Translator.objects.filter(id= translator_id)[0]
	authors = Author.objects.filter(book__translatorlink = translator)
	publishers = Publisher.objects.filter(book__translatorlink = translator)
	works = Work.objects.filter(book__translatorlink = translator)
	return render_to_response("translator_template.html", {'translator' : translator, 'authors' : authors, 'publishers' : publishers, 'works' : works})

def publisherpage(request, publisher_id):
	publisher = Publisher.objects.filter(id = publisher_id)[0]
	authors = Author.objects.filter(book__publisherlink = publisher)
	translators = Translator.objects.filter(book__publisherlink = publisher)
	works = Work.objects.filter(book__publisherlink = publisher)
	# series = Series.objects.filter(book__publisherlink = publisher)
	# copyrights_held = 
	return render_to_response("publisher_template.html", {'publisher' : publisher, 'authors' : authors, 'translators' : translators, 'works' : works})
	
def authorlist(request):
	authors = Author.objects.all().order_by('name')
	return render_to_response("author_list.html", {'authors':authors})

def publisherlist(request):
	publishers = Publisher.objects.all().order_by('name')
	return render_to_response("publisher_list.html", {'publishers':publishers})
	
def translatorlist(request):
	translators = Translator.objects.all().order_by('name')
	return render_to_response("translator_list.html", {'translators':translators})
	
def worklist(request):
	works = Work.objects.all().order_by('name')
	return render_to_response("work_list.html", {'works': works})
	
def booklist(request):
	books = Book.objects.all().order_by('title')
	return render_to_response("book_list.html", {'books':books})
	
#def base(request):
#	return render_to_response("base.html")
    
