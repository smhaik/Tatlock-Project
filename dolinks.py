from TatlockBooks.BookExhibit.models import Author, Publisher, Translator, Work, Book

def link():
    books = Book.objects.all()

    for book in books:
        author = Author.objects.get(name=book.author)
        print author
        book.authorlink = author
        work = Work.objects.get(name=book.work)
        print work
        book.worklink = work
        publisher = Publisher.objects.get(name=book.publisher)
        print publisher
        book.publisherlink = publisher
        translator = Translator.objects.get(name=book.translation)
        print translator
        book.translatorlink = translator
        book.save()
