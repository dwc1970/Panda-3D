from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3


class MyApp ( ShowBase ) :
    def __init__(self) :
        ShowBase.__init__ ( self )

        # Cargar el modelo
        self.character = self.loader.loadModel ( "path/to/your/model.bam" )
        self.character.reparentTo ( self.render )

        # Cargar la animación
        self.character.loop ( "walk" )

        # Posicionar el modelo
        self.character.setPos ( Point3 ( 0 , 10 , 0 ) )


app = MyApp ( )
app.run ( )
