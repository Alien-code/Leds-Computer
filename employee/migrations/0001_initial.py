# Generated by Django 2.1.1 on 2018-11-21 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('designation', models.CharField(max_length=60)),
                ('address', models.TextField()),
                ('nid', models.CharField(default='Not given yet!', max_length=60)),
                ('contact', models.CharField(max_length=15)),
                ('joining_date', models.DateField(blank=True)),
            ],
        ),
    ]
