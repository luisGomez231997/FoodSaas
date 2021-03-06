# Generated by Django 3.1.1 on 2020-10-28 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_total', models.FloatField(blank=True, default=0.0, null=True)),
                ('iva', models.FloatField(blank=True, default=0.0, null=True)),
                ('total', models.FloatField(blank=True, default=0.0, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'bill',
                'verbose_name_plural': 'bills',
                'db_table': 'bill',
            },
        ),
    ]
