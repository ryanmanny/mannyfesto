from django.db import models

from core import models as core_models


class CribbagePost(core_models.Post):
    detail_view_name = 'cribbage_post'

    text = models.TextField()  # To use unicode cards
