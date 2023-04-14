# Generated by Django 4.1 on 2023-04-10 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_delete_reportuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Offline', max_length=35, verbose_name='Статус водія в ParkFleet')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.driver')),
            ],
        ),
    ]