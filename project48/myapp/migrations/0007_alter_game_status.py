# Generated by Django 3.2.8 on 2021-10-25 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_game_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(blank=True, choices=[('W', 'WIN'), ('L', 'LOSE'), ('T', 'TIE')], max_length=5, null=True),
        ),
    ]
