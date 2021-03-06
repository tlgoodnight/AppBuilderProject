# Generated by Django 2.2.5 on 2022-02-11 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtvTrails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trail_name', models.CharField(blank=True, default='', max_length=50)),
                ('vehicle_type', models.CharField(choices=[('ATV', 'ATV'), ('Motorcycle', 'Motorcycle'), ('Side by Side', 'Side by Side')], max_length=50)),
                ('trail_distance', models.DecimalField(decimal_places=0, default='', max_digits=4)),
                ('trail_terrain', models.CharField(choices=[('Grass', 'Grass'), ('Dirt', 'Dirt'), ('Concrete', 'Concrete'), ('Gravel', 'Gravel'), ('Sand', 'Sand'), ('Woodchips', 'Woodchips')], max_length=50)),
                ('trail_description', models.TextField(default='', max_length=500)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
