# Generated by Django 3.0.4 on 2020-04-04 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eTutor', '0003_auto_20200401_0418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.PositiveIntegerField()),
                ('dm', models.PositiveIntegerField()),
                ('friend', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='private',
            field=models.BooleanField(default=True),
        ),
    ]
