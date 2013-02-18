from TatlockBooks.BookExhibit.models import Author, Publisher, Translator, Work, Book

def burst():
    books = Book.objects.all()
    valuelist = Book.objects.values_list('author')
    authors = list(set([i[0] for i in valuelist]))
    valuelist = Book.objects.values_list('work')
    works = list(set([i[0] for i in valuelist]))
    valuelist = Book.objects.values_list('publisher')
    publishers = list(set([i[0] for i in valuelist]))
    valuelist = Book.objects.values_list('translation')
    translators = list(set([i[0] for i in valuelist]))

    print "\nAUTHORS"
    for authname in authors:
        author, created = Author.objects.get_or_create(name=authname)
        print author, created

    print "\nWORKS"
    for workname in works:
        work, created = Work.objects.get_or_create(name=workname)
        print work, created

    print "\nPUBLISHERS"
    for publishername in publishers:
        publisher, created = Publisher.objects.get_or_create(name=publishername)
        print publisher, created

    print "\nTRANSLATORS"
    for translatorname in translators:
        translator, created = Translator.objects.get_or_create(name=translatorname)
        print translator, created
