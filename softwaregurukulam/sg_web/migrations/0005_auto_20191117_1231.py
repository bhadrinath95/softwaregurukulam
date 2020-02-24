# Generated by Django 2.2.7 on 2019-11-17 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sg_web', '0004_auto_20191117_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
