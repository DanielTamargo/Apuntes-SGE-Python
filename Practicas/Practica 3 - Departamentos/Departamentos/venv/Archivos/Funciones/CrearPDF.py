import time
from datetime import datetime
import locale
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

import reportlab
#from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.platypus import Table
from reportlab.platypus import TableStyle

def crearPDF(venta):
    doc = SimpleDocTemplate("PDF/prueba.pdf",
                            title="Lista Productos",
                            pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)

    Story = []

    logotipo = "logo-empresa-small.png"

    locale.setlocale(locale.LC_TIME, 'es_ES')
    ahora = datetime.today()
    ahora = ahora.strftime("%A, %d de %B %Y %H:%M:%S")
    #formatoFecha = time.ctime()
    formatoFecha = str(ahora).title()
    formatoFecha = formatoFecha.replace("De", "de")


    imagen = Image(logotipo, 1 * inch, 1 * inch)
    Story.append(imagen)
    Story.append(Spacer(1, 20))
    estilos = getSampleStyleSheet()
    estilos.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    texto = '%s' % formatoFecha
    Story.append(Paragraph(texto, estilos["Normal"]))
    Story.append(Spacer(1, 12))

    texto = 'Estimado/a cliente,'
    Story.append(Paragraph(texto, estilos["Normal"]))
    Story.append(Spacer(1, 12))

    texto = "¡Gracias por su compra!\n" \
            "Como aquí, en Artic Gaming, valoramos completamente a nuestros clientes,\n" \
            "queremos dejar a su disposición la factura para que disponga\n" \
            "de toda la información del pedido.\n" \
            "Para cualquier duda o problema, no dude en contactarnos."

    texto = '¡Gracias por su compra! \
            Como aquí, en Artic Gaming, valoramos completamente a nuestros clientes, \
            queremos dejar a su disposición la factura para que disponga, \
            de toda la información del pedido. \
            Para cualquier duda o problema, no dude en contactarnos.'

    Story.append(Paragraph(texto, estilos["Justify"]))
    Story.append(Spacer(1, 24))

    ############################  TABLA  ############################
    # 0) Preparamos los datos y la tabla

    #ventas = cd.cargar_datos_ventas()
    #venta = ventas[0] #### <- seleccionar una venta en concreto
    productos = venta.productos

    #data = [
    #    ['          Producto          ', '          Precio          ', '          Precio total          '],
    #    ['Producto', 'Precio', ''],
    #    ['Producto', 'Precio', ''],
    #    ['Producto', 'Precio', ''],
    #    ['', '', 'Precio total :)']
    #]

    data = [
        ['          Producto          ', '          Precio          ', '          Precio total          ']
    ]

    for producto in productos:
        datos = []
        datos.append(str(producto.nombre))
        datos.append(str(producto.precio))
        datos.append("")
        data.append(datos)
    data.append(["", "", str(venta.precio_total)])

    table = Table(data)

    # 1) Preparamos el estilo

    style = TableStyle([
        ('BACKGROUND', (0, 0), (3, 0), colors.lightskyblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.darkblue),

        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),

        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),

        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),

        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])
    table.setStyle(style)

    # 2) Alternando color de fondo de las filas
    rowNumb = len(data)
    for i in range(1, rowNumb):
        if i % 2 == 0:
            bc = colors.lightblue
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

    Story.append(table)
    Story.append(Spacer(1, 24))
    texto = 'De nuevo, gracias por su compra.'
    Story.append(Paragraph(texto, estilos["Justify"]))
    Story.append(Spacer(1, 48))
    texto = 'Sinceramente,'
    Story.append(Paragraph(texto, estilos["Normal"]))
    Story.append(Spacer(1, 12))
    texto = 'Daniel Tamargo, Artic Gaming CEO'
    Story.append(Paragraph(texto, estilos["Normal"]))
    Story.append(Spacer(1, 12))

    doc.build(Story)

