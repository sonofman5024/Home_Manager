# Generated by Django 3.1.6 on 2021-02-27 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claim', '0002_auto_20210214_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claimlist',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Declined', 'Declined'), ('NEW', 'New Claim')], default='NEW', max_length=10),
        ),
    ]