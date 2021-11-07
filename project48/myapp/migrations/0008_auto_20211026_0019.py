# Generated by Django 3.2.8 on 2021-10-25 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_game_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='level',
            field=models.CharField(blank=True, choices=[('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'), ('ADVANCED', 'Advanced')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(blank=True, choices=[('WIN', 'Win'), ('LOSE', 'Lose'), ('TIE', 'Tie')], max_length=5, null=True),
        ),
    ]
