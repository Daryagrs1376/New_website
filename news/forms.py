from django import forms
from .models import ReporterProfile, Comment, Subtitle, User

class ReporterProfileForm(forms.ModelForm):
    class Meta:
        model = ReporterProfile
        fields = ['reporter', 'phone']

class AddCategoryForm(forms.Form):
    title = forms.CharField(max_length=255, label='عنوان')
    main_category = forms.ChoiceField(choices=[(1, 'Category 1'), (2, 'Category 2')])  
    selectcategory= forms.CharField()
    main_category = forms.ChoiceField(
        choices=[
            (1, 'sport'),
            (2, 'economy'),
            (3, 'iran'),
            (4, 'world'),
            (5, 'politics'),
            (6, 'culture'),
        ],
        label='انتخاب دسته‌بندی اصلی',
        required=True,
    )
    add_button = forms.BooleanField(required=False, label='افزودن')
    close_button = forms.BooleanField(required=False, label='بستن')

class EditCategoryForm(forms.Form):
    onvan_news = forms.CharField(max_length=255, label='عنوان خبر', required=True)
    short_description = forms.CharField(widget=forms.Textarea, label='توضیح کوتاه', required=True)
    add_media = forms.FileField(required=False, label='اضافه کردن رسانه')
    remove_media = forms.BooleanField(required=False, label='حذف رسانه')
    category = forms.ChoiceField(choices=[(1, 'Category 1'), (2, 'Category 2')]) 
    keywords = forms.CharField(max_length=255)
    record_news = forms.BooleanField(required=False)    
    
class SubtitleForm(forms.ModelForm):
    class Meta:
        model = Subtitle
        fields = ['subtitle_title']

    def clean_subtitle(self):
        subtitle = self.cleaned_data.get('subtitle')
        if len(subtitle) < 85:
            raise forms.ValidationError('زیرنویس باید حداقل 85 حرف باشد.')
        return subtitle
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content'] 
        
