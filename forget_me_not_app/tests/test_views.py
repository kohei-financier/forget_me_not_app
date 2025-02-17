from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from forget_me_not_app.models import Memo, Category
from django.utils import timezone

class MemoTests(TestCase):
    
    def setUp(self):
        # 基本的なデータを作成する
        self.user = User.objects.create_user(username='test1', password='password')
        self.category = Category.objects.create(name="テスト")
        self.client.login(username='test1', password='password')
    
    def test_create_memo_authenticated(self):
        # 権限があるユーザーがメモを作れるか
        response = self.client.post(reverse('forget_me_not_app:new_memo'), {
            'title': 'メモのテスト',
            'text': 'メモメモメモメモ',
            'reminder_time': timezone.now() + timezone.timedelta(days=1),
            'categories': [self.category.id],
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Memo.objects.filter(title='メモのテスト').exists()) #メモがあるかの確認

    def test_create_memo_unauthenticated(self):
        # 他のユーザーがメモを触れないようにできているか確認
        self.client.logout()
        response = self.client.post(reverse('forget_me_not_app:new_memo'), {
            'title': 'このメモは作れないはず',
            'text': '作れたら困る…。',
            'reminder_time': timezone.now() + timezone.timedelta(days=1),
            'categories': [self.category.id],
        })
        self.assertEqual(response.status_code, 302) #リダイレクトされていたらOK。
    
    def test_delete_memo_authenticated(self):
        # 権限があるユーザーがメモを消せるか
        memo = Memo.objects.create(title="消せるメモのはず", owner=self.user, reminder_time=timezone.now() + timezone.timedelta(days=1))
        response = self.client.post(reverse('forget_me_not_app:delete_memo', kwargs={'memo_id': memo.id}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Memo.objects.filter(id=memo.id).exists()) #存在していないことをassertFalseで確認する

    def test_delete_memo_forbidden(self):
        another_user = User.objects.create_user(username='anotheruser', password='password')
        memo = Memo.objects.create(title="消せないからリダイレクトさせるぜ", owner=another_user, reminder_time=timezone.now() + timezone.timedelta(days=1))
        response = self.client.post(reverse('forget_me_not_app:delete_memo', kwargs={'memo_id': memo.id}))
        self.assertRedirects(response, reverse('forget_me_not_app:memos'))   #リダイレクトされていたらOK。
    
    def test_edit_memo_authenticated(self):
        # 認証されたユーザーが自分のメモを編集できるかテスト
        memo = Memo.objects.create(title="こーーーれは編集できるメモです", owner=self.user, reminder_time=timezone.now() + timezone.timedelta(days=1))
        response = self.client.post(reverse('forget_me_not_app:edit_memo', kwargs={'memo_id': memo.id}), {
            'title': '編集しました。見れてる？',
            'text': '編集したのだ。',
            'reminder_time': timezone.now() + timezone.timedelta(days=2),
        })
        self.assertEqual(response.status_code, 302)
        memo.refresh_from_db()
        self.assertEqual(memo.title, '編集しました。見れてる？')

    def test_edit_memo_forbidden(self):
        another_user = User.objects.create_user(username='anotheruser', password='password')
        memo = Memo.objects.create(title="見れねえメモ", owner=another_user, reminder_time=timezone.now() + timezone.timedelta(days=1))
        response = self.client.post(reverse('forget_me_not_app:edit_memo', kwargs={'memo_id': memo.id}), {
            'title': '更新できない',
            'text': '更新できないはずだよ～',
            'reminder_time': timezone.now() + timezone.timedelta(days=2),
        })
        self.assertEqual(response.status_code, 404)

