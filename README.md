# django-service

Proyecto base Django con Docker Compose y Dev Containers.

## Stack
- Django 6
- PostgreSQL 18
- Docker Compose
- Dev Container (VS Code)
- Gestor de dependencias: `uv`

## Estructura de entornos
- `dev`: `db_dev` + `web_dev`
- `prod-like`: `db_prod` + `web_prod`

## Variables de entorno
Archivo de referencia:
- `.env.example`

Archivos locales (no versionados):
- `.env.dev`
- `.env.prod`

## Flujo recomendado (VS Code Dev Container)
1. Abrir proyecto en VS Code.
2. Verificar `/.devcontainer/devcontainer.json`:
   - Dev: `service: "web_dev"` y `runServices: ["db_dev", "web_dev"]`
   - Prod-like: `service: "web_prod"` y `runServices: ["db_prod", "web_prod"]`
3. Ejecutar `Dev Containers: Rebuild and Reopen in Container` solo cuando cambie infraestructura.

## Docker Compose (terminal)

### Levantar servicios
```bash
# Dev
docker compose up -d --build db_dev web_dev

# Prod-like
docker compose up -d --build db_prod web_prod

# Todos (no recomendado para trabajo diario)
docker compose up -d --build
```

### Detener y limpiar
```bash
# Detener todo
docker compose down

# Detener y borrar volúmenes
docker compose down -v

# Detener solo prod-like
docker compose stop db_prod web_prod
```

### Logs y estado
```bash
docker compose ps
docker compose logs -f web_dev
docker compose logs -f db_dev
```

## Comandos Django útiles
```bash
# Migraciones
docker compose exec web_dev python manage.py makemigrations
docker compose exec web_dev python manage.py migrate

# Admin
docker compose exec web_dev python manage.py createsuperuser

# Shell Django
docker compose exec web_dev python manage.py shell

# Revisión básica de proyecto
docker compose exec web_dev python manage.py check

```

## Cuándo usar rebuild
No hace falta rebuild por cambios de código (Python/HTML/CSS/JS).
Usa rebuild cuando cambies:
- `Dockerfile`
- `docker-compose.yml`
- archivos en `.devcontainer/`
- dependencias (`pyproject.toml`, `uv.lock`)

## Primer arranque rápido
```bash
cp .env.example .env.dev
cp .env.example .env.prod
docker compose up -d --build db_dev web_dev
docker compose exec web_dev python manage.py migrate
docker compose exec web_dev python manage.py createsuperuser
```
