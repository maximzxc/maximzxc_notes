from django.db import models

# Create your models here.


class Note(models.Model):
    '''
    Every Note have title, content, date of adding and update date

    title field created for Notes captions
    content field created for text that they contains
    added shows when Note was added to database
    updated shows when Note was edited, if it wasn't edited it shows
    same that 'added' field

    #Create some notes
    >>> note1 = Notes.objects.create(title='qwe', content='asdasd')
    >>> note2 = Notes.objects.create(title='zxc', content='asd123asd')

    #Show title of Note
    >>>note1.title

    #Show content of Note
    >>>note2.content
    '''
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='img', null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __unicode__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=255)
    notes = models.ManyToManyField(Note)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __unicode__(self):
        return self.title
