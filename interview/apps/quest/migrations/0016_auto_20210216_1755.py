# Generated by Django 2.2.10 on 2021-02-16 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0015_auto_20210216_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answeroption',
            name='question',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='quest.Question'),
        ),
        migrations.AlterField(
            model_name='resulta',
            name='result',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='quest.Result'),
        ),
    ]
