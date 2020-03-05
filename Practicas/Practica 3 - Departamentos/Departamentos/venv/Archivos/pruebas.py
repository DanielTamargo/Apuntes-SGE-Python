import os
from datetime import date
from datetime import datetime
import Archivos.Funciones.CargarDatos as cd
import Archivos.Clases as Clases

import reportlab
#from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.platypus import Table
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import TableStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

logo = 'logo-empresa-small.jpg'

ahora = datetime.today()
ahora = ahora.strftime("%d-%m-%Y_%H-%M-%S")

pdf3 = SimpleDocTemplate(
    "PDF/tablav2.pdf",
    title="Tabla Productos del Pedido",
    pagesize=letter,
    rightMargin=72,
    leftMargin=72,
    topMargin=72,
    bottomMargin=18
)
Story = []

titulo = "Tabla de productos del pedido"

imagen = Image(logo, 1*inch, 1*inch)
Story.append(imagen)

estilos = getSampleStyleSheet()
estilos.add(ParagraphStyle(name='Justify', aligment=TA_JUSTIFY))
texto = str(ahora)
Story.append(Paragraph(texto, estilos["Normal"]))
Story.append(Spacer(1, 12))

texto = "Estimado/a cliente, gracias por su compra\n" \
        "Como aquí, en Artic Gaming, valoramos completamente a nuestros clientes,\n" \
        "queremos dejar a su disposición la factura para que disponga\n" \
        "de toda la información del pedido.\n" \
        "Para cualquier duda o problema, no dude en contactarnos."
Story.append(Paragraph(texto, estilos["Normal"]))
Story.append(Spacer(1, 12))












############################  TABLA  ############################
fileName2 = "PDF/tabla.pdf"
pdf2 = SimpleDocTemplate(
    fileName2,
    title="Tabla Productos del Pedido",
    pagesize=letter
)

elems = []

# 0) Preparamos los datos y la tabla

#ventas = cd.cargar_datos_ventas()
#venta = ventas[0]
#productos = venta.productos

data = [
    ['Producto', 'Precio', 'Precio total'],
    ['Producto', 'Precio', 'Precio total'],
    ['Producto', 'Precio', 'Precio total'],
    ['Producto', 'Precio', 'Precio total']
]

#for producto in productos:
#    datos = []
#    datos.append(str(producto.nombre))
#    datos.append(str(producto.precio))
#    datos.append("")
#    data.append(datos)
#data.append(["", "", str(venta.precio_total)])

table = Table(data)

# 1) Preparamos el estilo

style = TableStyle([
    ('BACKGROUND', (0, 0), (3, 0), colors.orange),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),

    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),

    ('FONTNAME', (0, 0), (-1, 0), 'Courier-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),

    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),

    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
])
table.setStyle(style)

# 2) Alternando color de fondo de las filas
rowNumb = len(data)
for i in range(1, rowNumb):
    if i % 2 == 0:
        bc = colors.burlywood
    else:
        bc = colors.beige

    ts = TableStyle(
        [('BACKGROUND', (0, i), (-1, i), bc)]
    )
    table.setStyle(ts)

# 3) Bordes
ts = TableStyle(
    [
        ('BOX', (0, 0), (-1, -1), 2, colors.black),
        ('LINEBEFORE', (2, 1), (2, -1), 2, colors.red),
        ('LINEABOVE', (0, 2), (-1, 2), 2, colors.green),
        ('GRID', (0, 1), (-1, -1), 2, colors.black),
    ]
)
table.setStyle(ts)
elems.append(table)
pdf2.build(elems)


ahora = datetime.today()
ahora = ahora.strftime("%d-%m-%Y_%H-%M-%S")

#fileName = 'PDF/pdf_{0}.pdf'.format(str(ahora))
#documentTitle = 'PDF Factura ' + str(venta.id)
#title = 'Factura pedido: ' + str(venta.id)
#subTitle = '¡Esperamos volver a contar contigo pronto!'

'''
fileName = 'PDF/pdf.pdf'
documentTitle = 'PDF Factura afsdf'
title = 'Factura pedido: afsdf'
subTitle = '¡Esperamos volver a contar contigo pronto!'


textLines = [
    'Estimado/a cliente, gracias su compra.',
    'Como aquí, en Artic Gaming, valoramos completamente a nuestros clientes,',
    'queremos dejar a tu disposición la factura para que disponga ',
    'de toda la información del pedido.',
    'Quedamos a su disposición para cualquier duda o problema que pueda surgir.'
]

logo = 'logo-empresa-small.jpg'

pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)

# Titulo
pdf.setFont("Helvetica-Bold", 28)
pdf.drawString(30, 770, title)
#pdf.drawCentredString(180, 770, title)

# Logo
pdf.drawImage(logo, 500, 570)


# Subtítulo
pdf.setFillColorRGB(43, 153, 255)
pdf.setFont("Helvetica", 14)
pdf.drawCentredString(290, 720, subTitle)

# Línea separatoria
pdf.line(30, 710, 550, 710) #pinta una línea de x y hasta x2 y2

# Texto
text = pdf.beginText(30, 680)
text.setFont("Courier", 12)
text.setFillColor(colors.black)
for line in textLines:
    text.textLine(line)
pdf.drawText(text)
pdf.save()
'''

