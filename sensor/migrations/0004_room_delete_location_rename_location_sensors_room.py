# Generated by Django 4.1.6 on 2023-02-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0003_personincharge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('floor', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.RenameField(
            model_name='sensors',
            old_name='location',
            new_name='room',
        ),
    ]
