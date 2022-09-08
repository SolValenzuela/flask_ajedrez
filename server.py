from flask import Flask, render_template
app= Flask(__name__)

#Haz que otra ruta acepte un solo parámetro (es decir, "/") 
# y renderiza un tablero de ajedrez con x cantidad de filas, con colores alternos
@app.route('/')
def tablero_completo():
    return render_template('tablero.html',x=8,y=8, color1="red",color2="black")



#BONUS NINJA: Haz que otra ruta acepte 2 parámetro (es decir, "//") 
# y renderiza un tablero de ajedrez con x filas e y columnas Las columnas, con colores alternos
@app.route('/<int:x>/<int:y>')
def tablero_medio(x,y):
   return render_template('tablero.html',x=x,y=y, color1="red",color2="black")

#BONUS SENSEI: Haz que otra ruta acepte 4 parámetro (es decir, "////") 
# y renderiza un tablero de ajedrez con x filas e y columnas, con colores alternos, color1 y color2
@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def tablero_de_colores(x,y,color1,color2):
   return render_template('tablero.html',x=x,y=y, color1=color1,color2=color2)

if __name__=="__main__":
    app.run(debug=True)