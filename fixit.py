from TatlockBooks.BookExhibit.models import Book, Bookimage

def fix():
	books = Book.objects.all()
	for book in books:
		if book.id <28:
			bookimages = book.bookimage_set.all()
			for bookimage in bookimages:
				parsed = bookimage.image.name.split("/")
				bookimage.image.name = parsed[1]
				print bookimage.image.name
				#bookimage.save()
			
