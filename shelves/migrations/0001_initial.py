# Generated by Django 3.1 on 2020-08-23 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=1000, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='recommendations', to='books.book')),
                ('from_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sent_recommendations', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='recommendations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
