from django.shortcuts import render
from .models import Memo
# Create your views here.
def index(request):
    """忘れ物メモのTOPページ（兼 ログイン画面）"""
    return render(request, 'forget_me_not_app/index.html')

def memos(request):
    """忘れ物メモの一覧ページ"""
    memos = Memo.objects.order_by('created_at')
    context = {"memos": memos}
    return render(request, 'forget_me_not_app/memos.html', context)

# 編集画面で使うかも！
# def memo(request, memo_id):
#     """1つ1つのメモを表示する"""
#     memo = Memo.objects.get(id=memo_id)
    