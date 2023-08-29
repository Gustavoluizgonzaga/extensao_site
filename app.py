from flask import Flask, render_template

app = Flask(__name__)

# definindo a página homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

# definindo a página contato
@app.route('/contato')
def contato():
    return render_template('contato.html')

# definindo usuario
@app.route('/usuario''/<nome_usuario>')
def usuario(nome_usuario):
    return render_template('usuario.html')


# colocar o site no ar
if __name__ == '__main__':
    app.run(debug=True)
