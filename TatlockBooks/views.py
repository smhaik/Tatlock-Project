from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.models import Q
from django.template import RequestContext
from BookExhibit.models import Book, Author, Publisher, Translator, Work, Series, Bookimage, Extraimage
import simplejson as json
import re


def home(request):
	authors = Author.objects.all().order_by('name')
	publishers = Publisher.objects.all().order_by('name')
	translators = Translator.objects.all().order_by('name')
	books = Book.objects.all().order_by('title')
	works = Work.objects.all().order_by('name')
	series = Series.objects.all().order_by('name')
	inscriptions = Book.objects.filter(inscription__isnull = False).order_by('title')
	illustrations = Book.objects.filter(has_illustrations = True).order_by('title')
	marginalia = Book.objects.filter(bookimage__is_marginalia=True).order_by('title')
	inserts = Book.objects.filter(bookimage__is_insert = True).order_by('title')
	backmatter = Book.objects.filter(has_backmatter = True).order_by('title')
	
	return render_to_response("Home.html",{'authors' : authors, 'publishers' : publishers, 'translators' : translators, 'books' : books, 'works' : works, 'series': series, 'illustrations':illustrations, 'inserts':inserts, 'inscriptions':inscriptions, 'marginalia':marginalia, 'backmatter':backmatter})
    
def welcome(request):
	return render_to_response("welcome.html")
	
def contact(request):
	return render_to_response("contact.html")
	
def about(request):
	return render_to_response("about.html")	
    
def bookpage(request, book_label):
	book = Book.objects.filter(label=book_label)[0]
	bookimages = book.bookimage_set.all()
	firstimage = bookimages[0].name_only()
	works = book.worklink.all()
	translators = book.translatorlink.all()
	return render_to_response("book_template.html", {'book': book, 'bookimages':bookimages, 'works': works, 'firstimage': firstimage, 'translators':translators})

def workpage(request, work_id):
	work = Work.objects.filter(id = work_id)[0]
	translators = Translator.objects.filter(book__worklink = work).distinct()
	publishers = Publisher.objects.filter(book__worklink = work).distinct()
	books = Book.objects.filter(worklink = work).distinct()
	return render_to_response("work_template.html", {'work' : work, 'translators':translators, 'publishers':publishers, 'books':books})

def seriespage(request, series_id):
	series = Series.objects.filter(id = series_id)[0]
	books = Book.objects.filter(serieslink = series)
	creator = Publisher.objects.filter(book__serieslink = series)
	return render_to_response("series_template.html", {'series' : series, 'creator':creator, 'books':books})	
	 
def authorpage(request, author_id):
	author = Author.objects.filter(id = author_id)[0]
	publishers = Publisher.objects.filter(book__author = author).distinct()
	translators = Translator.objects.filter(book__author = author).distinct()
	works = Work.objects.filter(book__author = author).distinct()
	return render_to_response("author_template.html", {'author' : author, 'publishers' : publishers, 'translators' : translators, 'works' : works})

def translatorpage(request, translator_id):
	translator = Translator.objects.filter(id= translator_id)[0]
	publishers = Publisher.objects.filter(book__translatorlink = translator).distinct()
	works = Work.objects.filter(book__translatorlink = translator).distinct()
	authors = Author.objects.filter(work__book__translatorlink = translator).distinct()
	return render_to_response("translator_template.html", {'translator' : translator, 'authors' : authors, 'publishers' : publishers, 'works' : works})

def publisherpage(request, publisher_id):
	publisher = Publisher.objects.filter(id = publisher_id)[0]
	authors = Author.objects.filter(work__book__publisherlink = publisher).distinct()
	translators = Translator.objects.filter(book__publisherlink = publisher).distinct()
	works = Work.objects.filter(book__publisherlink = publisher).distinct()
	series = Series.objects.filter(book__publisherlink = publisher).distinct()
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
	pythonhash = {}
	for book in books:
		pythonhash[book.id] = [o.name_only() for o in book.bookimage_set.all()]
	bookimages = json.dumps(pythonhash)									
	return render_to_response("book_list.html", {'books':books, 'bookimages': bookimages})
	
def serieslist(request):
	series = Series.objects.all().order_by('name')
	return render_to_response("series_list.html", {'series':series})
	
def marginalia(request):
	marginalia = Book.objects.filter(bookimage__is_marginalia = True).order_by('title')
	pythonhash = {}
	for book in marginalia:
		pythonhash[book.id] = [o.name_only() for o in book.bookimage_set.all()]
	bookimages = json.dumps(pythonhash)	
	return render_to_response("marginalia.html", {'marginalia':marginalia, 'bookimages':bookimages})

def illustrations(request):
	illustrations = Book.objects.filter(has_illustrations = True).order_by('title')
	pythonhash = {}
	for book in illustrations:
		pythonhash[book.id] = [o.name_only() for o in book.bookimage_set.all()]
	bookimages = json.dumps(pythonhash)	
	return render_to_response("illustrations.html", {'illustrations':illustrations, 'bookimages':bookimages})
	
def inscriptions(request):
	inscriptions = Book.objects.filter(inscription__isnull = False).order_by('title')
	pythonhash = {}
	for book in inscriptions:
		pythonhash[book.id] = [o.name_only() for o in book.bookimage_set.all()]
	bookimages = json.dumps(pythonhash)	
	return render_to_response("inscriptions.html", {'inscriptions':inscriptions, 'bookimages':bookimages})
	
def backmatter(request):
	backmatter = Book.objects.filter(has_backmatter = True).order_by('title')
	pythonhash = {}
	for book in backmatter:
		pythonhash[book.id] = [o.image.name for o in book.bookimage_set.all()]
	bookimages = json.dumps(pythonhash)	
	return render_to_response("backmatter.html", {'backmatter':backmatter, 'bookimages':bookimages})

def inserts(request):
	inserts = Book.objects.filter(bookimage__is_insert = True).order_by('title')
	pythonhash = {}
	for book in inserts:
		pythonhash[book.id] = [o.name_only() for o in book.bookimage_set.all()]
	bookimages = json.dumps(pythonhash)	
	return render_to_response("inserts.html", {'inserts':inserts, 'bookimages':bookimages})

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):

    return [(normspace(' ', (t[0] or t[1]).strip())) for t in findterms(query_string)]

def get_query(query_string, search_fields):
  # Returns a query, that is a combination of Q objects. That combination
  # aims to search keywords within a model by testing the given search fields.
    
	# Query to search for every search term  
	query = None       
	terms = normalize_query(query_string)
	for term in terms:
		# Query to search for a given term in each field
		or_query = None
		for field_name in search_fields:
			q = Q(**{"%s__icontains" % field_name: term})
			if or_query is None:
				or_query = q
			else:
				or_query = or_query | q
		if query is None:
			query = or_query
		else:
			query = query | or_query
	return query
	
def search(request):
	query_string = ''
	found_books = None
	found_authors = None
	found_translators = None
	found_publishers = None
	found_series = None
	found_work = None
	if ('q' in request.GET) and request.GET['q'].strip():
		query_string = request.GET['q']
		book_query = get_query(query_string, ['title', 'work', 'author', 'publisher', 'translation', 'pubplace','year', 'series','inscription', 'inscription_date', 'recent_copyright', 'recent_copyright_date', 'edition','physdesc','notes'])
		found_books = Book.objects.filter(book_query).order_by('title')
		author_query = get_query(query_string, ['name', 'birth_date', 'death_date', 'year_start', 'year_end', 'description'])
		found_authors = Author.objects.filter(author_query).order_by('name')
		translator_query = get_query(query_string, ['name', 'birth_date', 'death_date', 'year_start', 'year_end', 'description'])
		found_translators = Translator.objects.filter(translator_query).order_by('name')
		publisher_query = get_query(query_string, ['name', 'year_start', 'year_end', 'location', 'description'])
		found_publishers = Publisher.objects.filter(publisher_query).order_by('name')
		series_query = get_query(query_string, ['name', 'creator',])
		found_series = Series.objects.filter(series_query).order_by('name')
		work_query = get_query(query_string, ['name', 'description'])
		found_works = Work.objects.filter(work_query).order_by('name')
		
		return render_to_response('searchresults.html', {'query_string':query_string,'book_query':book_query, 'found_books':found_books,'author_query':author_query,'found_authors':found_authors, 'translator_query':translator_query, 'found_translators':found_translators, 'publisher_query':publisher_query,'found_publishers':found_publishers, 'series_query':series_query,'found_series':found_series})
	
	redirect_request('Home.html')

#def base(request):
#	return render_to_response("base.html")
    
