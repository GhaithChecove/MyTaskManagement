# Generated by Django 4.2.2 on 2023-06-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tsk_is_finished',
            field=models.BooleanField(default=False, verbose_name='Is Finished'),
        ),
    ]
