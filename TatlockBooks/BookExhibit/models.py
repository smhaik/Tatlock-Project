from django.db import models

class Publisher(models.Model):
	name = models.CharField(max_length=100)
	logo = models.ImageField(upload_to='/media_root/logos/')
	year_start = models.IntegerField(null = True)
	year_end = models.IntegerField(null = True)
	location = models.CharField(max_length = 100, blank = True)
	description = models.TextField(blank=True, default='')
	#series/collections by this publisher
		# see "views.py"
	ads = models.ImageField(upload_to='/media_root/ads/')
	def letter(self):
		return self.name[0]
		
	def __unicode__(self):
		return self.name

class Author(models.Model):
	name = models.CharField(max_length=100)
	birth_date = models.IntegerField( null = True)
	death_date = models.IntegerField(null = True)
	year_start = models.IntegerField(null = True)
	year_end = models.IntegerField(null = True)
	description = models.TextField(blank=True, default='')
	portrait = models.ImageField(upload_to='/media_root/portraits/')
	def letter(self):
		return self.name[0]
		
	def __unicode__(self):
		return self.name

class Work(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, null=True)
    description = models.TextField(blank=True, default='')
    #editions of this work: see views.py

    def letter(self):
		return self.name[0]
		
    def __unicode__(self):
        return self.name
    
class Translator(models.Model):
	name = models.CharField(max_length=100)
	portrait = models.ImageField(upload_to='/media_root/portraits/')
	birth_date = models.IntegerField(null = True)
	death_date = models.IntegerField(null = True)
	year_start = models.IntegerField(null = True)
	year_end = models.IntegerField(null = True)
	description = models.TextField(blank=True, default='')
	translatorads = models.ImageField(upload_to='/media_root/ads/')
	def letter(self):
		return self.name[0]
		
	def __unicode__(self):
		return self.name
        
class Series(models.Model):
	name = models.CharField(max_length = 100)
	creator = models.ForeignKey(Publisher)
	#books in series: see views.py
	
	def __unicode__(self):
		return self.name
	
class Book(models.Model):
	label = models.CharField(max_length=20)
	title = models.CharField(max_length=100)
	work = models.CharField(max_length=100)
	worklink = models.ManyToManyField(Work, null=True)
	author = models.CharField(max_length=100)
	publisher = models.CharField(max_length=100)
	publisherlink = models.ForeignKey(Publisher, null=True)
	pubplace = models.CharField(max_length=100)
	year = models.IntegerField(null = True)
	copyright = models.TextField(max_length=500)
	copyright_date = models.IntegerField(null = True)
	recent_copyright = models.CharField(max_length = 254)
	recent_copyright_date = models.IntegerField(null = True)
	translation = models.CharField(max_length=100)
	translatorlink = models.ManyToManyField(Translator, null=True)
	pages = models.CharField(max_length=40)
	series = models.CharField(max_length=100)
	serieslink = models.ForeignKey(Series, null = True)
	edition = models.CharField(max_length=100)
	physdesc = models.TextField()
	inscription = models.TextField()
	inscription_date = models.IntegerField(blank = True)
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
		ordering = [ 'label']
        

class Bookimage(models.Model):
	image = models.ImageField(upload_to='/media_root/bookimages/')
	book = models.ForeignKey(Book)
	sequence = models.IntegerField()
	page = models.CharField(max_length = 100)
	type_choices = (
		(u'spine', u'spine'),
		(u'fcover', u'front cover'), 
		(u'bcover', u'back cover'), 
		(u'inscription', u'inscription'),
		(u'titlepage', u'title page'),
		(u'copypage', u'copyrights page'),
		(u'first_text', u'first page of text'),
		(u'second_text', u'second page of text'),
		(u'second_last_text', u'second to last page of text'),
		(u'last_text', u'last page of text'),
		(u'special', u'special'), 
	)
	is_frontispiece = models.BooleanField(default=False)
	is_table_contents = models.BooleanField(default=False)
	is_back_ad = models.BooleanField(default=False)
	is_back_cat = models.BooleanField(default=False)
	is_illustration = models.BooleanField(default=False)
	is_marginalia = models.BooleanField(default=False)
	is_insert = models.BooleanField(default=False)
	
	def __unicode__(self):
		return u"----- {0} ----- {1}".format(self.image, self.book)
	class Meta:
		ordering = ['image', 'book']

class Extraimage(models.Model):
	book = models.ForeignKey(Book)
	image = models.ImageField(upload_to='/media_root/extraimages/')
	type_choice = (
		(u'portrait', u'portrait'),
		(u'logo', u'logo'),
		(u'other', u'other'),
	)	
 
	def __unicode__(self):
		return u"----- {0} ----- {1}".format(self.image, self.book)
	class Meta:
		ordering = ['image', 'book']
