# Generated by Django 3.1.1 on 2020-10-24 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purcharse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('pay', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bills.bill')),
            ],
            options={
                'verbose_name': 'payment',
                'verbose_name_plural': 'payments',
                'db_table': 'payment',
            },
        ),
    ]
