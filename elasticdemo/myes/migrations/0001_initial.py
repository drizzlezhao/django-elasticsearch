# Generated by Django 2.2 on 2019-04-05 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('img_url', models.CharField(max_length=1024)),
                ('content', models.TextField()),
                ('uid', models.CharField(max_length=64)),
                ('blog_tag', models.ForeignKey(on_delete=True, to='myes.Tag')),
            ],
        ),
    ]
