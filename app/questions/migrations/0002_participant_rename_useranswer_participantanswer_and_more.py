# Generated by Django 5.0.6 on 2024-06-17 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='UserAnswer',
            new_name='ParticipantAnswer',
        ),
        migrations.CreateModel(
            name='QuizAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.participant')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.quiz')),
            ],
        ),
        migrations.AlterField(
            model_name='participantanswer',
            name='attempt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questions.quizattempt'),
        ),
        migrations.DeleteModel(
            name='UserQuizAttempt',
        ),
    ]