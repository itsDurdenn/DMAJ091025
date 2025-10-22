from flask import Flask, render_template,request, redirect, url_for,session, flash

app= Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'

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

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        nombreCompleto = request.form['nombreCompleto']
        email = request.form['email']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']
        fechaNacimiento = request.form['fechaNacimiento']
        genero = request.form['genero']
        biografia = request.form['biografia']
        checkNotificaciones = request.form.get('checkNotificaciones')
        checkTerminos = request.form.get('checkTerminos')
        
        if password != confirmPassword:
            flash('Las contraseñas no coinciden. Por favor, inténtalo de nuevo.', 'danger')
            return render_template('sesion.html')
        
        session['usuario'] = nombreCompleto
        flash(f'Inicio de sesión exitoso para el usuario: {nombreCompleto}', 'success')
        
        return redirect(url_for('inicio'))
    
    return render_template('sesion.html')
if __name__ == '__main__':
    app.run(debug=True)