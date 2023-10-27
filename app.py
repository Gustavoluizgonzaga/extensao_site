from flask import Flask, render_template
app = Flask(__name__)

# definindo a página homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

# definindo a página de produtos
@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/produtos/<nome_produto>')
def produto(nome_produto):
    return render_template('produto.html', nome_produto=nome_produto)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')

@app.route('/receitas')
def receitas():
    return render_template('receitas.html', receitas=receitas)

if __name__ == '__main__':
    app.run(debug=True)
