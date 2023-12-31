# Generated by Django 4.2 on 2023-07-01 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tables', '0033_old_debt'),
    ]

    operations = [
        migrations.CreateModel(
            name='BigTableRows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_count', models.IntegerField(default=0, null=True)),
                ('total_price', models.IntegerField(default=0, null=True)),
                ('bigTable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.bigtable')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier1', to=settings.AUTH_USER_MODEL)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.usertable')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='WeekTables',
        ),
    ]
