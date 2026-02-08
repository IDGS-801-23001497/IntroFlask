from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect

import forms
import math

app = Flask(__name__)
app.secret_key='clave secreta'
csrf=CSRFProtect()

@app.route("/")
def index():
    titulo="Flask IDGS801"
    lista=["Juan","Mario","Pedro","Dario"]
    return render_template("index.html", titulo=titulo, lista=lista)
    

@app.route("/operasBas", methods=["GET", "POST"])
def operas1():
    n1=0
    n2=0
    res=0
    if request.method =='POST':
        n1=request.form.get('n1')
        n2=request.form.get('n2')
        res= float(n1)+float(n2)
    return render_template("operasBas.html",n1=n1,n2=n2,res=res)


@app.route("/resultado", methods=['GET', 'POST'])
def resultado():
    n1=request.form.get('n1')
    n2=request.form.get('n2')
    tem= float(n1)+float(n2)
    return f"la suma es: {tem}"

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")


@app.route("/usuarios", methods =["GET","POST"])

def usuarios():
    mat=0
    nom=''
    apa=''
    ama=''
    correo=''
    usuarios_class=forms.UserForm(request.form)
    if request.method =='POST':
        mat=usuarios_class.matricula.data
        nom=usuarios_class.nombre.data
        apa=usuarios_class.apaterno.data
        ama=usuarios_class.amaterno.data
        correo=usuarios_class.correo.data

    return render_template("usuarios.html", form=usuarios_class,
                           mat=mat, nom=nom, apa=apa, ama=ama, correo=correo)


@app.route('/cinepolis', methods=["GET", "POST"])
def cinepolis():
    Nombre = ""
    Compradores = 0
    tarjCine = ""
    Boletos = 0
    total = 0
    error = None
    cinepolis_class=forms.CinepolisForm(request.form)

    if request.method == "POST" and cinepolis_class.validate():
        Nombre = cinepolis_class.nombre.data
        Compradores = cinepolis_class.compradores.data
        tarjCine = cinepolis_class.tarjeta.data
        Boletos = cinepolis_class.boletos.data

        if not Boletos or not Compradores:
            error = "Error: Debes ingresar un número de boletos o compradores."
            return render_template('cinepolis.html', form=cinepolis_class, error=error, total=total)
        
        if Boletos > Compradores * 7:
            error = "Error: No se pueden comprar más de 7 boletos por comprador."
            return render_template('cinepolis.html', form=cinepolis_class, error=error, total=total)
        
        total = Boletos * 12
        if Boletos > 5:
            total = total - (total * 0.15)  # Aplicar descuento del 15% si son 5 boletos
        if Boletos >= 3 and Boletos <= 5:
            total = total - (total * 0.10)  # Aplicar descuento del 10% si son entre 3 y 5 boletos

        if tarjCine == "true":
            total = total - (total * 0.10)  # Aplicar descuento del 10% por tarjeta Cinépolis
        print(total)
    return render_template('cinepolis.html', form=cinepolis_class,Nombre=Nombre, Compradores=Compradores, tarjCine=tarjCine, Boletos=Boletos, total=total)

@app.route('/distancia', methods=["GET", "POST"])
def distancia():
    x1=0
    x2=0
    y1=0
    y2=0
    res=0
    if request.method == "POST":
        x1=int(request.form.get("x1"))
        x2=int(request.form.get("x2"))
        y1=int(request.form.get("y1"))
        y2=int(request.form.get("y2"))
        res = float(math.sqrt(((x2 - x1)*(x2-x1) + (y2 - y1)*(y2 - y1))))
    return render_template('distancia.html',x1=x1,x2=x2,y1=y1,y2=y2,res=res)


@app.route("/hola")
def hola():
    return "Hola, mundo!, geis y lesbianas "

@app.route("/user/<string:user>")
def user(user):
    return f"Hello, {user}!"

@app.route("/numero/<int:n>")
def numero(n):
    return f"<h1>EL numero es:{n}</h1>"

@app.route("/user/<int:id>/<string:username>")
def usernamer(id,username):
    return f"<h1>¡Hola, {username}! Tu ID es:{id}</h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"<h1> la suma es {n1+n2}</h1>"


@app.route("/default/")
@app.route("/default/<string:parm>")
def func(param="juan"):
    return f"<h1> ¡Hola, {param}! </h1>"


@app.route("/operas/")
def operas():
    return '''

<form>
<label for="name">Name:</label>
<input type="text" id="name name="name" required></input>
</br>
<label for="name">paterno:</label>
<input type="text" id="name name="name" required></input>
</form>
'''
if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug= True)