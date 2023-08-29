
# Definimos nuestra clase linea que hereda de Flowable
class linea(Flowable):

    # Inicializamos la clase Flowable con los datos que llegan desde el que llama la clase  
    # definimos h que el la altura de la linea como 0 ya que la linea no tiene volumen  
    def __init__(self,w,h=0):
        Flowable.__init__(self)
        self.width = w
        self.height = h

    # dibujamos la linea en el canvas
    # No se especifica ni x ni y porque platypus se encarga de ponerla donde la necesitemos
    def draw(self):
        self.canv.line(0, self.height, self.width, self.height)


@codigoreportes

