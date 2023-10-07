# Generated by Django 4.2.6 on 2023-10-06 08:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]