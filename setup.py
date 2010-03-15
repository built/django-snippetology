from distutils.core import setup

setup(
    name='snippetology',
    description='A text snippet manager for Django',
    author='Matt Youell',
    author_email='matt@youell.com',
    url='http://code.google.com/p/django-snippetology/',
    packages=[
        'snippetology',
        'snippetology.templatetags',
    ],
)
