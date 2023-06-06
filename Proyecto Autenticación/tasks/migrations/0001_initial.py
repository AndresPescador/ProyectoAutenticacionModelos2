from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('ID_Permiso', models.BigAutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('ID_Rol', models.BigAutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=15)),
                ('Otros_atributos', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=180)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(blank=True, default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('ID_Usuario', models.BigAutoField(primary_key=True, serialize=False)),
                ('Nombres', models.CharField(max_length=15)),
                ('Apellidos', models.CharField(max_length=15)),
                ('Contrasena', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Relacion_Usuario_Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Rol', models.ManyToManyField(to='todo_api.rol')),
                ('ID_Usuario', models.ManyToManyField(to='todo_api.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Relacion_Rol_Permiso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Permiso', models.ManyToManyField(to='todo_api.permiso')),
                ('ID_Rol', models.ManyToManyField(to='todo_api.rol')),
            ],
        ),
    ]

