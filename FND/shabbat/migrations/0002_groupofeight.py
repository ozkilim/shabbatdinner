# Generated by Django 2.1.3 on 2019-04-16 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shabbat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupOfEight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organiser_name_a', models.CharField(max_length=100)),
                ('organiser_name_b', models.CharField(max_length=100)),
                ('organiser_email_a', models.CharField(max_length=100)),
                ('organiser_email_b', models.CharField(max_length=100)),
            ],
        ),
    ]