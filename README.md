# Validador de Archivos CSV

Aplicación web en Django para validar la estructura de archivos CSV.

## Requisitos

- Python 3.8+

## Instalación

```bash
# Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install django
```

## Ejecución

```bash
python manage.py runserver
```

Abrir http://127.0.0.1:8000 en el navegador.

## Uso

1. Seleccionar o arrastrar un archivo CSV
2. Clic en "Validar"
3. Ver resultados: errores por fila/columna o mensaje de éxito

## Reglas de Validación

| Columna | Validación |
|---------|------------|
| 1 | Números enteros, 3-10 dígitos |
| 2 | Correo electrónico válido |
| 3 | Solo "CC" o "TI" |
| 4 | Valor entre 500.000 y 1.500.000 |
| 5 | Cualquier valor |

## Estructura

```
csv_validator/
├── csv_validator/     # Configuración Django
│   ├── settings.py
│   └── urls.py
├── validator/         # App principal
│   └── views.py       # Lógica de validación
├── templates/
│   └── upload.html    # Interfaz
└── manage.py
```
