# Generated by Django 5.0.6 on 2024-06-21 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_course_student'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='teacher',
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ManyToManyField(to='teacher.teacher'),
        ),
    ]
