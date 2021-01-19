# Generated by Django 3.0.1 on 2021-01-18 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realestate_store', '0002_realestate_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_num', models.IntegerField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('payed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='ItemOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_order_p', to='order.Order')),
                ('realestate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_order_a', to='realestate_store.RealEstate')),
            ],
        ),
    ]
