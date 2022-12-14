# Generated by Django 4.1 on 2022-08-25 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Notice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('aothor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notice.notice')),
            ],
        ),
    ]
