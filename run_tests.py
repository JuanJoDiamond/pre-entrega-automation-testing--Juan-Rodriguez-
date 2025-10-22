import pytest
import datetime # Para manejar fechas y horas en el nombre del reporte

# Se crea una lista de los archivos de las pruebas a ejecutar
test_files = [
    "tests/test_login.py",
    "tests/test_inventory.py"
]

# Argumentos para ejecutar las pruebas: archivos + reporte HTML
pytest_args = test_files + ["--html=report.html","--self-contained-html","-v"]

# Personalizar el nombre del reporte con fecha y hora
pytest_args.append("--html=reports/report.html")
now = datetime.datetime.now()
timestamp = now.strftime("%Y%m%d_%H%M")
report_filename = f"reports/report_{timestamp}.html"
pytest_args[ -1] = f"--html={report_filename}"
# Ejecutar pytest con los argumentos especificados
print(pytest_args)

pytest.main(pytest_args)
