# Generated by Django 3.1.7 on 2021-04-09 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                               related_name='question_ID', to='home.question')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                          related_name='tag_ID', to='home.tag')),
            ],
        ),
        migrations.AddConstraint(
            model_name='question_tag',
            constraint=models.UniqueConstraint(fields=('question', 'tag'), name='question_tag'),
        ),
    ]
