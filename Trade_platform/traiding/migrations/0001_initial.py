# Generated by Django 3.2.7 on 2021-11-04 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Items', '0010_alter_watchlist_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_quantity', models.IntegerField(verbose_name='Requested quantity')),
                ('order_type', models.PositiveSmallIntegerField(choices=[('1', 'buy'), ('2', 'sell')])),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Items.item')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
