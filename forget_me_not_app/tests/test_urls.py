from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from forget_me_not_app.models import Memo, Category
from datetime import timedelta
from django.utils import timezone

class TestUrls(TestCase):

    def setUp(self):
        """セットアップ"""
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.memo = Memo.objects.create(
            title="テスト通りますように！",
            text="テスト通りますように！",
            owner=self.user,
            reminder_time=timezone.now() + timedelta(days=1)
        )
        self.category = Category.objects.create(name="カテゴリラ")

    def test_homepage_url(self):
        """ホームページのURLが正しく動作するか確認"""
        response = self.client.get(reverse('forget_me_not_app:index'))
        self.assertEqual(response.status_code, 200)

    def test_memos_url(self):
        """メモ一覧ページのURLが正しく動作するか確認"""
        response = self.client.get(reverse('forget_me_not_app:memos'))
        self.assertEqual(response.status_code, 200)

    def test_new_memo_url(self):
        """新規メモ作成ページのURLが正しく動作するか確認"""
        response = self.client.get(reverse('forget_me_not_app:new_memo'))
        self.assertEqual(response.status_code, 200)

    def test_edit_memo_url(self):
        """メモ編集ページのURLが正しく動作するか確認"""
        response = self.client.get(reverse('forget_me_not_app:edit_memo', args=[self.memo.id]))
        self.assertEqual(response.status_code, 200)

    def test_new_category_url(self):
        """新規カテゴリー追加ページのURLが正しく動作するか確認"""
        response = self.client.get(reverse('forget_me_not_app:new_category'))
        self.assertEqual(response.status_code, 200)

    def test_edit_category_url(self):
        """カテゴリー編集ページのURLが正しく動作するか確認"""
        response = self.client.get(reverse('forget_me_not_app:edit_category', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_memo_url(self):
        """メモ削除ページのURLが正しく動作するか確認"""
        response = self.client.get(reverse('forget_me_not_app:delete_memo', args=[self.memo.id]))
        self.assertEqual(response.status_code, 200)
