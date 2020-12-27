# Generated by Django 2.1.5 on 2020-12-27 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authuser',
            old_name='userID',
            new_name='username',
        ),
        migrations.AddField(
            model_name='authuser',
            name='email',
            field=models.EmailField(default=None, max_length=254, null=True, verbose_name='メールアドレス'),
        ),
        migrations.AddField(
            model_name='authuser',
            name='first_name',
            field=models.CharField(default=None, max_length=30, verbose_name='名前'),
        ),
        migrations.AddField(
            model_name='authuser',
            name='last_name',
            field=models.CharField(default=None, max_length=30, verbose_name='苗字'),
        ),
    ]
