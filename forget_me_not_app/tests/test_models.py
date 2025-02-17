from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from ..models import Memo, Category

class TestModels(TestCase):
    
    def test_is_empty(self):
        """初期状態でデータが入っていないことのチェック"""
        saved_memos = Memo.objects.all()
        saved_categories = Category.objects.all()
        self.assertEqual(saved_memos.count(), 0)
        self.assertEqual(saved_categories.count(), 0)
        
    def test_is_count_one(self):
        """適当にレコードを作成して、カウントされることを確認！"""
        test_user = User.objects.create_user(username='test', password='password')
        category = Category.objects.create(name='aaaa')
        memo = Memo(title='tekitou', text='tekitouaaaaa', reminder_time = timezone.make_aware(datetime(2025, 10, 10, 0, 0)), owner=test_user)
        memo.save()
        memo.categories.add(category)
        saved_memos = Memo.objects.all()
        saved_categories = Category.objects.all()
        self.assertEqual(saved_memos.count(),1)
        self.assertEqual(saved_categories.count(),1)
        self.assertIn(category,memo.categories.all())
        
    def test_category_str(self):
        """strメソッド>nameを返すか"""
        category = Category.objects.create(name='仕事関係')
        self.assertEqual(str(category), '仕事関係')

    def test_memo_str(self):
        """strメソッド>Titleを返すか"""
        test_user = User.objects.create_user(username='test', password='password')
        memo = Memo.objects.create(
            title='aiueo',
            text='aaaaaaaaaaaaaaaaaaaaaa',
            reminder_time = timezone.make_aware(datetime(2025, 10, 10, 0, 0)),
            owner=test_user
        )
        self.assertEqual(str(memo), 'aiueo')
        
    def test_memo_deletion(self):
        """Memoが削除できるか"""
        test_user = User.objects.create_user(username='test', password='password')
        category = Category.objects.create(name='Work')
        memo = Memo.objects.create(
            title='aiueo',
            text='aaaaaaaaaaaaaaaaaaaaaa',
            reminder_time = timezone.make_aware(datetime(2025, 10, 10, 0, 0)),
            owner=test_user
        )
        memo.categories.add(category)
        memo.delete()
        self.assertEqual(Memo.objects.count(), 0)
        # Categoryは消えてないよね？
        self.assertEqual(Category.objects.count(), 1)

