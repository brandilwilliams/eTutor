# Generated by Django 3.0.4 on 2020-04-06 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eTutor', '0005_auto_20200406_0522'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
