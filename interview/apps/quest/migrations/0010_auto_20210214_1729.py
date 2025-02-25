# Generated by Django 2.2.10 on 2021-02-14 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0009_auto_20210214_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer_type',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Тип вопроса (1-ответ текстом, 2-выбор варианта, 3-выбор нескольких вариантов)'),
        ),
        migrations.AlterField(
            model_name='answeroption',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quest.Question'),
        ),
        migrations.AlterField(
            model_name='result_a',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quest.Result'),
        ),
    ]
