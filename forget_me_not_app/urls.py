"""app内のURLパターンの定義"""

from django.urls import path

from . import views

app_name = "forget_me_not_app"
urlpatterns = [
    # ホームページ
    path("", views.index, name="index"),
    # メモ一覧ページ
    path("memos/", views.memos, name="memos"),
    # メモ新規作成ページ
    path("new_memo/", views.new_memo, name="new_memo"),
    # メモ編集のページ
    path("memos/<int:memo_id>/", views.edit_memo, name="edit_memo"),
]
