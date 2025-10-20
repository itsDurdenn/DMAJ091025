from flask import Flask, render_template,request

app= Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html')  

@app.route('/animales')
def animales():
    return render_template('animales.html')

@app.route('/vehiculos')
def vehiculos():
    return render_template('vehiculos.html')    

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

@app.route('/signup')
def sign():
    return render_template('formulario.html')

@app.route('/signin')
def signin():
    return render_template('sesion.html')

if __name__ == '__main__':
    app.run(debug=True)