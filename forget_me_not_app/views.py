from django.shortcuts import render, redirect
from .models import Memo
from .forms import MemoForm


# Create your views here.
def index(request):
    """忘れ物メモのTOPページ（兼 ログイン画面）"""
    return render(request, "forget_me_not_app/index.html")


def memos(request):
    """忘れ物メモの一覧ページ"""
    memos = Memo.objects.order_by("created_at")
    context = {"memos": memos}
    return render(request, "forget_me_not_app/memos.html", context)


def new_memo(request):
    """メモ新規作成ページ"""

    if request.method != "POST":
        # データは送信されていないので空のフォームを用意する
        form = MemoForm
    else:
        # POSTでデータが送信された処理
        form = MemoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("forget_me_not_app:memos")

    # 空または無効のフォームを表示する
    context = {"form": form}
    return render(request, "forget_me_not_app/new_memo.html", context)


# 編集画面で使うかも！
# def memo(request, memo_id):
#     """1つ1つのメモを表示する"""
#     memo = Memo.objects.get(id=memo_id)
