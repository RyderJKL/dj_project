# Generated by Django 2.0.5 on 2018-05-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artile',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('article_heading', models.CharField(max_length=250)),
                ('atticle_body', models.TextField()),
            ],
        ),
    ]
