from django.db import models
from users.models import User
import datetime

class Question(models.Model):
    title = models.CharField(max_length= 500)
    body = models.TextField(max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, related_name='users_quesitons', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Question: {self.title} {self.body} {self.created_at}'


    class Meta:
        ordering: ['-created_at']


class Answer(models.Model):
    answer = models.ForeignKey(to=Question, related_name='answers', on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, related_name='users_answers', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Answer: {self.body} {self.created_at}'
    
    @property
    def get_favorite_count(self):
        return len(self.favorites.all())


class Favorite(models.Model):
    user = models.ForeignKey(to=User, related_name='favorites', on_delete=models.CASCADE)
    answer =models.ForeignKey(to=Answer, related_name='favorites', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} liked {self.answer}'