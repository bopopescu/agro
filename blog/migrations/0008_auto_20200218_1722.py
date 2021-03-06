# Generated by Django 3.0 on 2020-02-18 15:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200218_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='slug',
            field=models.SlugField(default='try', max_length=255, unique=True, verbose_name='Посилання на публікацію'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='slave',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='slave',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='slave',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='slave',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='slave',
            name='vacancy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Vacancy', verbose_name='Вакансія'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='activity',
            field=models.TextField(blank=True, null=True, verbose_name='Діяльність'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='adress',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Адреса'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Створено'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='requirements',
            field=models.TextField(blank=True, null=True, verbose_name='Вимоги'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Заголовок'),
        ),
    ]
