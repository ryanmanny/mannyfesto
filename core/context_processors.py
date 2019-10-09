from collections import namedtuple

from django.shortcuts import reverse


NavItem = namedtuple('NavItem', 'name link')


def header(request):
    return {
        'nav_items': [
            NavItem('Blog', reverse('blog')),
            NavItem('Short Stories', reverse('stories')),
            NavItem('About', reverse('about')),
        ]
    }
