# Generated by Django 2.2 on 2019-05-11 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=256)),
                ('pret', models.FloatField(default=1000.56)),
                ('descriere', models.CharField(default='Nu exista descriere', max_length=4096)),
            ],
        ),
    ]