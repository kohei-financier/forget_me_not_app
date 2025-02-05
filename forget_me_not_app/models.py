from django.db import models


# Create your models here.
class Memo(models.Model):
    """忘れ物メモを保存する"""

    title = models.CharField(max_length=20)
    text = models.TextField()
    reminder_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey("User", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.text


# ここにユーザーモデルは記載しない！（再利用性や複雑な認証をつけるなら別のAPPとして立ち上げたほうが良い）
