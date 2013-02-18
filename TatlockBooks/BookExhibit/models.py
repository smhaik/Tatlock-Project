from django.db import models

class Publisher(models.Model):
	name = models.CharField(max_length=100)
	#logo: image of this publishers logo/insignia if available
		#logo = FileBrowseField("Logo", max_length=200, #directory="images", extensions=[".jpg"], blank=True, null=True)
	years_active = models.CharField(max_length=100, blank = True)
	location = models.CharField(max_length = 100, blank = True)
	description = models.TextField(blank=True, default='')
	#series/collections by this publisher
		# see "views.py"
	#copyrights held by this publisher and dates
		#see "views.py"
	#advertisements; images of backmatter catalogues/advertisements hosted by this publisher
		#ads = FileBrowseField("Ads", max_length=200, #directory="images", extensions=[".jpg"], blank=True, null=True)
	def letter(self):
		return self.name[0]
		
	def __unicode__(self):
		return self.name

class Author(models.Model):
	name = models.CharField(max_length=100)
	birth_date = models.CharField(max_length=100, blank = True)
	death_date = models.CharField(max_length=100, blank = True)
	years_active = models.CharField(max_length=100, blank = True)
	description = models.TextField(blank=True, default='')
	#portrait = image of this author
	#series = any series by this author?
	def letter(self):
		return self.name[0]
		
	def __unicode__(self):
		return self.name

class Work(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, null=True)
    #hook work.author up to the author object
    description = models.TextField(blank=True, default='')
    #editions of this work (link to indiv books)?
    # what else do we want to know about the work?? 
    def letter(self):
		return self.name[0]
		
    def __unicode__(self):
        return self.name
    
class Translator(models.Model):
	name = models.CharField(max_length=100)
	#image of this translator if available
	birth_date = models.CharField(max_length=100, blank = True)
	death_date = models.CharField(max_length=100, blank = True)
	years_active = models.CharField(max_length =100, blank = True)
	description = models.TextField(blank=True, default='')
	#advertisements for this translator?? (A.L. Wister has a lot of them, don't remember if others do)
	def letter(self):
		return self.name[0]
		
	def __unicode__(self):
		return self.name
        
class Book(models.Model):
    label = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    worklink = models.ForeignKey(Work, null=True)
    author = models.CharField(max_length=100)
    authorlink = models.ForeignKey(Author, null=True)
    publisher = models.CharField(max_length=100)
    publisherlink = models.ForeignKey(Publisher, null=True)
    pubplace = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    copyright = models.CharField(max_length=254)
    copyright_date = models.CharField(max_length=254)
    translation = models.CharField(max_length=100)
    translatorlink = models.ForeignKey(Translator, null=True)
    pages = models.CharField(max_length=40)
    series = models.CharField(max_length=100)
    edition = models.CharField(max_length=100)
    physdesc = models.TextField()
    inscription = models.TextField()
    inscription_date = models.CharField(max_length=100)
    has_frontispiece = models.BooleanField(default=False)
    has_illustrations = models.BooleanField(default=False)
    has_backmatter = models.BooleanField(default=False)
    rdfpubid = models.CharField(max_length=100)
    notes = models.TextField()
    #in database: make notes more presentable
    #mark special pages of notes (marginalia, inserted material, etc)
		#include images of these and tag them to appear in a search result (deal with this when deal with search page)
    type = models.CharField(max_length=100)
    img_cover = models.CharField(max_length=100)
	
    def letter(self):
        return self.title[0]
		
    def __unicode__(self):
        return u"{0} {1} / {2} ({3})".format(self.label, self.work, self.author, self.year)
    class Meta:
        ordering = ['work', 'label']
        
#class series(models.Model):
	#name = models.CharField(max_length = 100)
	#creator = [[publisher]]/author: see views.py
	#books in series: see views.py

#class Bookimage(models.Model):
 #   image = FileBrowseField("Image", max_length=200, #directory="images", extensions=[".jpg"], blank=True, null=True)
 #   book = models.ForeignKey(Book)
 #image types: front/back cover, spine, inscription, frontispiece, titlepage, copyright, table of contents, first textpage, second text page, second-to-last text page, last text page, backmatter(advertisment/catalogue), illustration, marginalia, inserted material, portrait, logo
	#types are not all mutualy exclusive.
  #  def __unicode__(self):
   #     return u"----- {0} ----- {1}".format(self.image, self.book)
#    class Meta:
 #       ordering = ['image', 'book']
