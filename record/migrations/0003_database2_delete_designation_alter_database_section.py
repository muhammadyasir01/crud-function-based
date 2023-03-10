# Generated by Django 4.1.5 on 2023-02-11 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_designation_alter_database_designation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataBase2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=50)),
                ('designations', models.CharField(max_length=50)),
                ('sections', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='designation',
        ),
        migrations.AlterField(
            model_name='database',
            name='section',
            field=models.CharField(max_length=50),
        ),
    ]
