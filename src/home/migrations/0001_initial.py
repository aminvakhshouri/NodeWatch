# Generated by Django 2.2 on 2019-04-18 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=250)),
                ('val', models.TextField(blank=True)),
                ('is_encrypted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'variable',
                'managed': False,
            },
        ),
    ]