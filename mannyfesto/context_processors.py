from collections import namedtuple

from django.shortcuts import reverse


NavItem = namedtuple('NavItem', 'name link')


def header(request):
    return {
        'nav_items': [
            NavItem(
                'Non-Fiction',
                reverse(
                    'post_list',
                    kwargs={'category_slug': 'blog'},
                ),
            ),
            NavItem(
                'Fiction',
                reverse(
                    'post_list',
                    kwargs={'category_slug': 'stories'}),
            ),
            NavItem('About', reverse('about')),
        ]
    }
