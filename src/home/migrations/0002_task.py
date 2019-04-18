# Generated by Django 2.2 on 2019-04-18 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=155)),
                ('status', models.CharField(max_length=50)),
                ('traceback', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'celery_taskmeta',
                'managed': False,
            },
        ),
    ]