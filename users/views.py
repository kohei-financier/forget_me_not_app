from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """新規ユーザー登録"""
    if request.method != 'POST':
        # 空のユーザー登録フォームを表示する
        form = UserCreationForm()
    else:
        # 入力済みのフォームを処理する
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # ユーザーをログインさせてホームページにリダイレクトする
            login(request, new_user)
            return redirect('forget_me_not_app:memos')
    
    # 空または無効のフォームを表示する
    context = {'form': form}
    return render(request, 'registration/register.html', context)
    