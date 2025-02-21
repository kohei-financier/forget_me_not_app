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
    # 新規カテゴリー追加ページ
    path("new_category/", views.new_category, name="new_category"),
    # カテゴリー編集ページ
    path("edit_category/<int:category_id>/", views.edit_category, name="edit_category"),
    # メモ削除ページ
    path("delete_memo/<int:memo_id>/", views.delete_memo, name="delete_memo"),
    # カテゴリー削除ページ
    path("delete_category/<int:category_id>/", views.delete_category, name="delete_category"),
]
