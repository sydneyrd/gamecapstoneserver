# Generated by Django 4.1 on 2022-09-06 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamecapstoneapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='slot_user',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.RemoveField(
            model_name='question',
            name='solutions',
        ),
        migrations.AddField(
            model_name='question',
            name='solution',
            field=models.ManyToManyField(related_name='solved', through='gamecapstoneapi.QuestionSolution', to='gamecapstoneapi.solution'),
        ),
        migrations.AlterField(
            model_name='questionsolution',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamecapstoneapi.question'),
        ),
        migrations.AlterField(
            model_name='questionsolution',
            name='solution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamecapstoneapi.solution'),
        ),
        migrations.AlterField(
            model_name='slotuser',
            name='score',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='slotuser',
            name='title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_title', to='gamecapstoneapi.title'),
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
