# Generated by Django 5.0.6 on 2024-05-19 08:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('thoughts_for_the_day', models.TextField()),
                ('expectation', models.TextField()),
                ('reflection', models.TextField()),
                ('feeling', models.CharField(choices=[('anger', 'Anger'), ('frustrated', 'Frustrated'), ('happy', 'Happy'), ('calm', 'Calm'), ('numb', 'Numb'), ('sad', 'Sad'), ('excited', 'Excited')], max_length=10)),
                ('gratitude', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]