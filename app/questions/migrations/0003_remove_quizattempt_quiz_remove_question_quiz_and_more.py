# Generated by Django 5.0.6 on 2024-06-17 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_participant_rename_useranswer_participantanswer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizattempt',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
    ]
