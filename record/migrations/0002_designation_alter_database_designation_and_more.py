# Generated by Django 4.1.5 on 2023-02-11 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='database',
            name='designation',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='database',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='database',
            name='section',
            field=models.CharField(max_length=10),
        ),
    ]