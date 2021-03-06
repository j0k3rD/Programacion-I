from flask import Blueprint, render_template


#Crear Blueprint
poem = Blueprint('poem', __name__, url_prefix='/poem')

POEMS = [
            {"id":0,"poetname":"Pablo","title":"Red Roses","body":"Las rosas son rojas"},
            {"id":1,"poetname":"Facundo","title":"Boca vos sos mi pasion","body":"Con un marchete en la mano, con la chapa en el corazon, seras siempre independiente, vigilante y boton", "private":True},
            {"id":2,"poetname":"Emilia","title":"White Rose","body":"En el fin de los tiempos"},
            ]


@poem.route('/')
# def index():
#     #Mostrar template
#     return render_template('view_poem_poet.html')

@poem.route('/view/<int:id>')
def view(id):
    #Mostrar template
    return render_template('view_poem_poet.html')

