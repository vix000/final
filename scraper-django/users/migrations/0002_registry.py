# Generated by Django 2.1.5 on 2019-01-26 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_string', models.CharField(max_length=100, verbose_name='String that user was searching for')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='query time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registries', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
