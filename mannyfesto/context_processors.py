from collections import namedtuple

from django.shortcuts import reverse


NavItem = namedtuple('NavItem', 'name link')


def header(request):
    return {
        'nav_items': [
            NavItem(
                'Blog',
                reverse(
                    'post_list',
                    kwargs={'category_slug': 'blog'},
                ),
            ),
            NavItem(
                'Short Stories',
                reverse(
                    'post_list',
                    kwargs={'category_slug': 'stories'}),
            ),
            NavItem(
                'Cribbage',
                reverse(
                    'post_list',
                    kwargs={'category_slug': 'cribbage'},
                )
            ),
            NavItem('About', reverse('about')),
        ]
    }
