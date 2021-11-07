from django.db import models
from django.contrib.auth.models import User
from django.utils.html import  format_html
# Create your models here.

BOT_LEVE_CHOICE =(
    ('BEGINNER', 'Beginner'),
    ('INTERMEDIATE', 'Intermediate'),
    ('ADVANCED', 'Advanced')
)

class  Bot(models.Model):
    bot_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='upload/', null=True, blank=True)
    level = models.CharField(max_length =20, null=True, blank=True, choices=BOT_LEVE_CHOICE )
    def show_image(self):
        if self.image:
            return format_html('<img src="%s" height="40px" >' % self.image.url)
        else:
            return ''


WIN_CHOICE =(
    ('WIN', 'Win'),
    ('LOSE', 'Lose'),
    ('TIE', 'Tie')
)

class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=5, null=True, blank=True, choices=WIN_CHOICE)
    board1 = models.CharField(max_length=1)
    board2 = models.CharField(max_length=1)
    board3 = models.CharField(max_length=1)
    board4 = models.CharField(max_length=1)
    board5 = models.CharField(max_length=1)
    board6 = models.CharField(max_length=1)
    board7 = models.CharField(max_length=1)
    board8 = models.CharField(max_length=1)
    board9 = models.CharField(max_length=1)

