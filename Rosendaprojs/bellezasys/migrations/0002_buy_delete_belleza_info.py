# Generated by Django 4.0.3 on 2022-06-30 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bellezasys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=99)),
                ('lname', models.CharField(max_length=99)),
                ('age', models.IntegerField()),
                ('month', models.TextField(blank=True)),
                ('day', models.TextField(blank=True)),
                ('year', models.TextField(blank=True)),
                ('mode', models.TextField(blank=True)),
                ('code1', models.CharField(max_length=99)),
                ('quantity1', models.IntegerField()),
                ('price1', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Belleza_Info',
        ),
    ]
