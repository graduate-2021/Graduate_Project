# Generated by Django 2.2.4 on 2019-08-06 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='상품명')),
                ('price', models.IntegerField(verbose_name='가격')),
                ('stock', models.IntegerField(verbose_name='재고')),
                ('reg_date', models.DateField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': '상품',
                'verbose_name_plural': '상품',
                'db_table': 'products',
            },
        ),
    ]
