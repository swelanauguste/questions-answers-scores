# Generated by Django 5.0.6 on 2024-06-17 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_remove_quizattempt_quiz_remove_question_quiz_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantanswer',
            name='choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='questions.choice'),
        ),
        migrations.AlterField(
            model_name='participantanswer',
            name='is_correct',
            field=models.BooleanField(),
        ),
    ]