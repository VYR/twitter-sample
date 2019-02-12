# Generated by Django 2.0.9 on 2018-11-15 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0013_comment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Replycomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default=None, max_length=160)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/img')),
                ('replyid', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, related_name='cmtid', to='accounts.comment')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
