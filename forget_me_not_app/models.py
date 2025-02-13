from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    """カテゴリーを保存する"""

    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # モデル名を"Categories"に変更
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Memo(models.Model):
    """忘れ物メモを保存する"""

    title = models.CharField(max_length=20)
    text = models.TextField()
    reminder_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, null=True, blank=True)

    def __str__(self):
        return self.title

