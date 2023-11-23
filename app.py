from flask import Flask, render_template, request, redirect
app = Flask(__name__)

class influencer():
    def __init__(self,nome,plataforma,seguidores,interesse,imagem):
        self.nome = nome
        self.plataforma = plataforma
        self.seguidores = seguidores
        self.interesse = interesse
        self.imagem = imagem

@app.route('/')
def home():

    return render_template('Home.html', Influenciadores = lista)

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html')

@app.route('/criar',methods = ['POST'])
def criar():
    nome = request.form['nome']
    plataforma = request.form['plataforma']
    seguidores = request.form['seguidores']
    interesse = request.form['interesse']
    imagem = request.form['img']
    obj = influencer(nome,plataforma,seguidores,interesse,imagem )
    lista.append(obj)
    return redirect('/')
lista = []
if __name__ == '__main__':
    app.run()
