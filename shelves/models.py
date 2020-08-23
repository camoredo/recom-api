from django.db import models
from django.contrib.auth.models import User

from books.models import Book

RECOMMENDATION_STATUS_CHOICES = (
    (1, 'Pending'),
    (2, 'Accepted'),
    (3, 'Rejected'),
)


class Recommendation(models.Model):
    book = models.ForeignKey(
        Book, related_name="recommendations", on_delete=models.DO_NOTHING)
    to_user = models.ForeignKey(
        User, related_name="recommendations", on_delete=models.DO_NOTHING)
    from_user = models.ForeignKey(
        User,
        related_name="sent_recommendations",
        blank=True, null=True,
        on_delete=models.DO_NOTHING)
    message = models.TextField(max_length=1000, null=True, blank=True)
    status = models.IntegerField(
        choices=RECOMMENDATION_STATUS_CHOICES, default=1)
