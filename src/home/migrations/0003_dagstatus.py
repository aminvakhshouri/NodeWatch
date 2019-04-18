# Generated by Django 2.2 on 2019-04-18 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='DAGStatus',
            fields=[
                ('dag_id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=50, unique=True)),
                ('count', models.IntegerField(blank=True)),
            ],
            options={
                'db_table': 'dag_stats',
                'managed': False,
            },
        ),
    ]
