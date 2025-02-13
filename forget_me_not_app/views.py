from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Memo
from .forms import MemoForm


# Create your views here.
def index(request):
    """忘れ物メモのTOPページ（兼 ログイン画面）"""
    return render(request, "forget_me_not_app/index.html")

@login_required
def memos(request): # もしかしたらidが引数で必要かもしれない…。
    """忘れ物メモの一覧ページ"""
    memos = Memo.objects.filter(owner=request.user).order_by("created_at")
    
    # 現在のユーザーの投稿のみ表示
    # if memos.owner != request.user:
    #     raise Http404
    
    context = {"memos": memos}
    return render(request, "forget_me_not_app/memos.html", context)

@login_required
def new_memo(request):
    """メモ新規作成ページ"""

    if request.method != "POST":
        # データは送信されていないので空のフォームを用意する
        form = MemoForm
    else:
        # POSTでデータが送信された処理
        form = MemoForm(data=request.POST)
        if form.is_valid():
            new_memo = form.save(commit=False)
            new_memo.owner = request.user
            new_memo.save()
            return redirect("forget_me_not_app:memos")

    # 空または無効のフォームを表示する
    context = {"form": form}
    return render(request, "forget_me_not_app/new_memo.html", context)

@login_required
def edit_memo(request, memo_id):
    """メモ編集ページ"""
    memo = Memo.objects.get(id=memo_id)
    
    # 現在のユーザーの投稿のみ表示
    if memo.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = MemoForm(instance=memo)
    else:
        form = MemoForm(instance=memo, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('forget_me_not_app:memos')
    
    context = {'form': form, 'memo_id': memo.id}
    return render(request, 'forget_me_not_app/edit_memo.html', context)
