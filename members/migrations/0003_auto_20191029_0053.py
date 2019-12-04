# Generated by Django 2.2.3 on 2019-10-29 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20190724_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='current',
            name='bio',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
