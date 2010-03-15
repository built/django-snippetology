from snippetology.models import *
from django import template

register = template.Library()

@register.simple_tag
def snippet(snippet_name):
	"""
	Looks up a snippet by name and returns it.

	Syntax::

	    {% snippet [snippet_name] %}

	Example::

	    {% snippet frontpage_message %}

	"""

	return snip(snippet_name)

	
from django.template.defaultfilters import stringfilter
import random
		
@register.filter
@stringfilter
def random_line(value):
	"""
	Randomly selects a line out of a given bit of text. 
	Useful for rotating text like taglines, images tags w/ links, etc.
	Can be used as an ad rotator, etc.
	
	Example::

		{% filter random_line %}{% snippet tagline_list %}{% endfilter %}

	"""
	line_list = [line for line in value.splitlines() if len(line.strip()) > 0]
		
	if len(line_list) > 0: return random.choice(line_list)
			
	return ""

random_line.is_safe = True
