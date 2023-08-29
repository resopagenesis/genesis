
    reportsize = @reportsize
    nombre = '@modelo'
    nombrereporte = '@nombrereporte'
    orientacion = @orientacion
    margenes = [@ml,@mr,@mt,@mb] 
    font_titulo = '@fontTitulo'
    font_titulo_size = @fontTituloSize
    font_columnas = '@fontColumnas'
    font_columnas_size = @fontColumnasSize
    font = '@font'
    font_size = @fontSize
    font_encabezado = '@fontEncabezado'
    font_encabezado_size = @fontEncabezadoSize
    font_totales = '@fontTotales'
    font_totales_size = @fontTotalesSize

    doc = SimpleDocTemplate(nombrereporte + '.pdf', pagesize=orientacion(reportsize),leftMargin=margenes[0],
    rigthMargin=margenes[1],
    topMargin=margenes[2],
    bottomMargin=margenes[3])


    doc.font = font_encabezado
    doc.fontSize = font_encabezado_size

    historia = []

    maxpuntos = @maxpuntos - doc.leftMargin - doc.rightMargin
    # 792,612,841,595

    # estilos

    tbl_estilo_titulo = TableStyle([('FONT', (0, 0), (-1, -1), font_titulo),
                        ('FONTSIZE', (0, 0), (-1, -1), font_titulo_size),
                        ('VALIGN',(0,0),(1,-1),'MIDDLE')])

    tbl_estilo_texto = TableStyle([('VALIGN',(0,0),(1,-1),'MIDDLE')])

    ps_columnas = ParagraphStyle(name = 'Normal', fontSize = font_columnas_size, fontName=font_columnas)
    ps_texto = ParagraphStyle(name = 'Normal', fontSize = font_size, fontName=font)

    @barridomodelos

    doc.build(historia, onFirstPage=encabezado@modelo, onLaterPages=encabezado@modelo)
    # return HttpResponseRedirect('/@aplicacion/listar_@modelo')

