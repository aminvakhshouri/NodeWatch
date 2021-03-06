# Generated by Django 2.2 on 2019-04-18 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190418_0438'),
    ]

    operations = [
        migrations.CreateModel(
            name='DAGRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dag_id', models.CharField(max_length=250, unique=True)),
                ('execution_date', models.DateTimeField()),
                ('state', models.CharField(max_length=50)),
                ('run_id', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'dag_run',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='TaskInstance',
        ),
    ]
