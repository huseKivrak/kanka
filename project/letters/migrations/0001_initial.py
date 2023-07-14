# Generated by Django 4.2.3 on 2023-07-14 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('trackingmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.trackingmodel')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('sent', 'Sent'), ('delivered', 'Delivered'), ('read', 'Read')], default='draft', max_length=10)),
                ('sent_date', models.DateTimeField(blank=True, null=True)),
                ('delivery_date', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authored_letters', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(default=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authored_letters', to=settings.AUTH_USER_MODEL), null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_letters', to=settings.AUTH_USER_MODEL)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_letters', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('core.trackingmodel',),
            managers=[
                ('letters', django.db.models.manager.Manager()),
            ],
        ),
    ]