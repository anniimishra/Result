# Generated by Django 4.2.2 on 2023-06-25 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_subject_subjectmarks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjectmarks',
            old_name='std',
            new_name='student',
        ),
        migrations.AlterUniqueTogether(
            name='subjectmarks',
            unique_together={('student', 'subject')},
        ),
    ]
