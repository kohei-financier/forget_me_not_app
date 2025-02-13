from django import forms

from .models import Memo,Category

class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ("title", "text", "categories", "reminder_time")
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name",)
        