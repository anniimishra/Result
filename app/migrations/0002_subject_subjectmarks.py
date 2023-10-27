# Generated by Django 4.2.2 on 2023-06-25 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='subjectmarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('std', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentmarks', to='app.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subject')),
            ],
            options={
                'unique_together': {('std', 'subject')},
            },
        ),
    ]
