from django.forms import ModelForm
from froala_editor.widgets import FroalaEditor
from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']
        labels = {
            'content': '',
        }
        widgets = {
            'content': FroalaEditor()
        }