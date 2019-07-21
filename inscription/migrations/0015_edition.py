# Generated by Django 2.2.3 on 2019-07-20 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0014_auto_20180801_0301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('start_inscriptions', models.DateField(verbose_name='Start of Inscriptions')),
                ('end_inscriptions', models.DateField(verbose_name='End of Inscriptions')),
                ('start_edition', models.DateField(verbose_name='Start of Edition')),
                ('end_edition', models.DateField(verbose_name='End of Edition')),
                ('invitation', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
