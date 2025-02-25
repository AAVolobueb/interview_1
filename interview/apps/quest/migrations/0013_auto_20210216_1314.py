# Generated by Django 2.2.10 on 2021-02-16 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0012_auto_20210215_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answeroption',
            name='question',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='quest.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='interview',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='quest.Interview'),
        ),
        migrations.AlterField(
            model_name='resulta',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quest.Result'),
        ),
    ]
