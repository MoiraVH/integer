#!/usr/bin/env bash
# Instalar dependencias
pip install -r requirements.txt

# Comando adicional si es necesario
python manage.py collectstatic --noinput