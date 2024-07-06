# Generated by Django 5.0.6 on 2024-07-06 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('due_date', models.DateField(blank=True)),
                ('date_created', models.DateTimeField()),
                ('categories', models.CharField(choices=[('General', 'General'), ('Personal', 'Personal'), ('Work', 'Work')], default='General', max_length=20)),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Medium', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
