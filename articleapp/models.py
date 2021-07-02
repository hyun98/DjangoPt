from django.contrib.auth.models import User
from django.db import models
from froala_editor.fields import FroalaField

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True, related_name='article')

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', blank=True, null=True)
    content = FroalaField(plugins=('font_size', 'font_family'), null=True, blank=True, options={
        'toolbarInline': True,
    })
    created_at = models.DateField(auto_now_add=True, null=True)
