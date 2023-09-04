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

@app.route('/<nome_produto>')
def produto(nome_produto):
    return render_template('produto.html', nome_produto=nome_produto)



@app.route('/contato')
def contato():
    return render_template('contato.html')




# colocar o site no ar
if __name__ == '__main__':
    app.run(debug=True)
