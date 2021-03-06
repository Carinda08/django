# Generated by Django 3.2.4 on 2021-06-24 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('colorUrl', models.ImageField(upload_to='color/')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('oldPrice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='goods.category')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsDetailName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField()),
                ('color_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='goods.color')),
                ('good_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='goods.goods')),
                ('size_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='goods.size')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gdUrl', models.ImageField(upload_to='')),
                ('goodDetailName_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='goods.goodsdetailname')),
                ('good_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='goods.goods')),
            ],
        ),
    ]
