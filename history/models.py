from django.conf import settings
from django.db import models
from django.utils import timezone


class History(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="histories",
    )
    news = models.ForeignKey(
        "news.News",
        on_delete=models.CASCADE,
        related_name="histories",
    )
    view_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-view_time", "-id"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "news"],
                name="history_user_news_unique",
            )
        ]
        indexes = [
            models.Index(fields=["user"], name="history_user_idx"),
            models.Index(fields=["news"], name="history_news_idx"),
            models.Index(fields=["view_time"], name="history_view_time_idx"),
        ]

    def __str__(self):
        return f"{self.user_id}:{self.news_id}"
