# Generated by Django 4.0.6 on 2022-10-09 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_alter_comments_comment_code_alter_post_post_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='tweet',
        ),
        migrations.AlterField(
            model_name='post',
            name='post_code',
            field=models.CharField(default='4xnddntvky043hkee9jf', max_length=20),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('comment_code', models.CharField(default='43ge8pymfr8n9si535jz', max_length=100)),
                ('comment_date', models.DateField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
        ),
        migrations.AlterField(
            model_name='reply',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='blog.comment'),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
