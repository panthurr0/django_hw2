# Generated by Django 4.2.2 on 2024-05-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Контент')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='catalog/', verbose_name='Превью')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания (записи в БД)')),
                ('is_published', models.BooleanField(blank=True, default=False, null=True, verbose_name='Признак публикации')),
                ('views', models.IntegerField(blank=True, default=0, null=True, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
