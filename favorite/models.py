from django.conf import settings
from django.db import models
from django.utils import timezone


class Favorite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favorites",
    )
    news = models.ForeignKey(
        "news.News",
        on_delete=models.CASCADE,
        related_name="favorites",
    )
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at", "-id"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "news"],
                name="favorite_user_news_unique",
            )
        ]
        indexes = [
            models.Index(fields=["user"], name="favorite_user_idx"),
            models.Index(fields=["news"], name="favorite_news_idx"),
        ]

    def __str__(self):
        return f"{self.user_id}:{self.news_id}"
