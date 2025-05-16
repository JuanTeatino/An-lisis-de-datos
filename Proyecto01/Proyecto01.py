import os  # Importar la biblioteca os para manejar archivos del sistema

# Solicitar datos al usuario
Proyecto = input("Digita la descripcion del proyecto: ")  # Descripción del proyecto
Horas_estimadas = input("Digita la cantidad de horas estimadas: ")  # Horas estimadas para el proyecto
Valor_hora = input("Digita el valor de la hora trabajada: ")  # Valor por hora trabajada
Tiempo_estimado = input("Digita el tiempo estimado: ")  # Tiempo estimado en días o semanas
Valor_total = int(Horas_estimadas) * int(Valor_hora)  # Calcular el valor total del proyecto

from fpdf import FPDF  # Importar la biblioteca FPDF para generar PDFs

pdf = FPDF()  # Crear una instancia de FPDF

# Configuración del PDF
pdf.add_page()  # Agregar una página al PDF
pdf.set_font("Arial")  # Establecer la fuente del texto

# Agregar una imagen de fondo al PDF
pdf.image("Template.png", 0, 0)  # Insertar la imagen en la posición (0, 0)

# Agregar texto al PDF en posiciones específicas
pdf.text(115, 145, Proyecto)  # Descripción del proyecto
pdf.text(115, 160, Horas_estimadas)  # Horas estimadas
pdf.text(115, 175, Valor_hora)  # Valor por hora
pdf.text(115, 190, Tiempo_estimado)  # Tiempo estimado
pdf.text(115, 205, str(Valor_total))  # Valor total del proyecto

# Generar y guardar el archivo PDF
pdf.output("Presupuesto.pdf")  # Guardar el PDF con el nombre "Presupuesto.pdf"
print("Presupuesto generado con éxito!!!")  # Mensaje de confirmación

# Abrir el archivo PDF generado
os.startfile("Presupuesto.pdf")  # Abrir el PDF con el programa predeterminado del sistema