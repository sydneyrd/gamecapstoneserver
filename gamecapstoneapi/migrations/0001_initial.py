# Generated by Django 4.1 on 2022-09-02 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('visual', models.ImageField(null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=500)),
                ('difficulty', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SlotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.BigIntegerField()),
                ('session_score', models.BigIntegerField(null=True)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_title', to='gamecapstoneapi.title')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='gamecapstoneapi.question')),
                ('solution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solution', to='gamecapstoneapi.solution')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='solutions',
            field=models.ManyToManyField(related_name='question_solution', through='gamecapstoneapi.QuestionSolution', to='gamecapstoneapi.solution'),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('contact', models.CharField(max_length=200)),
                ('slot_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slot_user', to='gamecapstoneapi.slotuser')),
            ],
        ),
    ]