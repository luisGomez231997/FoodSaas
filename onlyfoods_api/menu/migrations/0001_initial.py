# Generated by Django 3.1.1 on 2020-10-24 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('franchise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('banner', models.CharField(blank=True, default='https://res.cloudinary.com/sigeedu/image/upload/v1594776164/sigedu/1528904524_boy_1_wehjsw.svg', max_length=2000, null=True)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('franchise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='menus', to='franchise.franchise')),
            ],
            options={
                'verbose_name': 'menu',
                'verbose_name_plural': 'menus',
                'db_table': 'menu',
            },
        ),
    ]
