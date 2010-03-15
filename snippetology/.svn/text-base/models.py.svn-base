from django.db import models

class Snippet(models.Model):

    title = models.CharField(max_length=64, unique=True)
    description = models.TextField(max_length=64, blank=True)
    content = models.TextField(blank=True)


    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
        

def snip(name):
	
	try:
		return Snippet.objects.get(title=name).content
	except:
		return ""
