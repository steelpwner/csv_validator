import csv
import re
from django.shortcuts import render


def validate_column1(value):
    """Solo debe permitir números enteros entre 3 y 10 caracteres"""
    if not re.match(r'^\d+$', value):
        return False, "Debe contener solo números enteros"
    if len(value) < 3 or len(value) > 10:
        return False, "Debe tener entre 3 y 10 caracteres"
    return True, None


def validate_column2(value):
    """Solo debe permitir correos electrónicos"""
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, value):
        return False, "Debe ser un correo electrónico válido"
    return True, None


def validate_column3(value):
    """Solo debe permitir los valores 'CC' o 'TI'"""
    if value not in ['CC', 'TI']:
        return False, "Solo se permiten los valores 'CC' o 'TI'"
    return True, None


def validate_column4(value):
    """Solo debe permitir valores entre 500000 y 1500000"""
    try:
        num = float(value)
        if num < 500000 or num > 1500000:
            return False, "Debe estar entre 500000 y 1500000"
        return True, None
    except ValueError:
        return False, "Debe ser un valor numérico"


def validate_column5(value):
    """Permite cualquier valor"""
    return True, None


def upload_file(request):
    context = {
        'errors': [],
        'success': False,
        'file_uploaded': False
    }

    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        context['file_uploaded'] = True

        if not csv_file.name.endswith('.csv'):
            context['errors'].append({
                'row': '-',
                'column': '-',
                'message': 'El archivo debe ser un archivo CSV'
            })
            return render(request, 'upload.html', context)

        try:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)

            validators = [
                validate_column1,
                validate_column2,
                validate_column3,
                validate_column4,
                validate_column5
            ]

            for row_num, row in enumerate(reader, start=1):
                if len(row) != 5:
                    context['errors'].append({
                        'row': row_num,
                        'column': '-',
                        'message': f'La fila debe tener exactamente 5 columnas. Tiene {len(row)} columnas.'
                    })
                    continue

                for col_num, (value, validator) in enumerate(zip(row, validators), start=1):
                    is_valid, error_msg = validator(value.strip())
                    if not is_valid:
                        context['errors'].append({
                            'row': row_num,
                            'column': col_num,
                            'message': error_msg
                        })

            if not context['errors']:
                context['success'] = True

        except Exception as e:
            context['errors'].append({
                'row': '-',
                'column': '-',
                'message': f'Error al procesar el archivo: {str(e)}'
            })

    return render(request, 'upload.html', context)
