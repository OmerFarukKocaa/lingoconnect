# Generated by Django 4.2.7 on 2023-12-07 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('correct_answer', models.CharField(max_length=15)),
                ('option1', models.CharField(max_length=15, null=True)),
                ('option2', models.CharField(max_length=15, null=True)),
                ('option3', models.CharField(max_length=15, null=True)),
                ('option4', models.CharField(max_length=15, null=True)),
                ('number_of_fails', models.IntegerField(null=True)),
                ('number_of_passes', models.IntegerField(null=True)),
                ('total_number', models.IntegerField(null=True)),
                ('category', models.CharField(max_length=15)),
                ('difficulty', models.CharField(max_length=15)),
                ('text1', models.CharField(max_length=200)),
                ('fail_percent', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizlist', models.TextField(null=True)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('succesrate', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('category', models.CharField(max_length=15)),
                ('difficulty', models.CharField(max_length=15)),
                ('q1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_requests_created10', to='app.question')),
                ('q10', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_requests_created1', to='app.question')),
                ('q2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_requests_created9', to='app.question')),
                ('q3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_requests_created8', to='app.question')),
                ('q4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_requests_created7', to='app.question')),
                ('q5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_requests_created6', to='app.question')),
                ('q6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_requests_created5', to='app.question')),
                ('q7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_requests_created4', to='app.question')),
                ('q8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_requests_created3', to='app.question')),
                ('q9', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_requests_created2', to='app.question')),
            ],
        ),
    ]
