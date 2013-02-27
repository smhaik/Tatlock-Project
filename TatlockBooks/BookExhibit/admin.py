from django.contrib import admin
from django.db import models
from django.forms import ModelForm
from models import Book, Author, Publisher, Work, Translator, Series, Bookimage, Extraimage
# filebrowser.settings import ADMIN_THUMBNAIL

from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
import os

class BookAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': (('label', 'title', ), 
            'author',
            ('publisher', 'pubplace', 'year'), 
            ('copyright', 'copyright_date', 'recent_copyright', 'recent_copyright_date'),
            ('translation', 'pages', 'series', 'edition'),
            ('physdesc', 'has_frontispiece', 'has_illustrations', 'has_backmatter'),
            ('inscription', 'inscription_date'),
            'rdfpubid',
            'notes', 
            )
        }),
    )    
#    formfield_overrides = {
#        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':80})},
#    }
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Translator)
admin.site.register(Work)
admin.site.register(Series)
admin.site.register(Bookimage)
admin.site.register(Extraimage)
