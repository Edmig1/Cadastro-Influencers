from flask import Flask, render_template, request, redirect
app = Flask(__name__)
cont = 0
class influencer():
    def __init__(self,nome,plataforma,seguidores,interesse,imagem,cont):
        self.nome = nome
        self.plataforma = plataforma
        self.seguidores = seguidores
        self.interesse = interesse
        self.imagem = imagem
        self.cont = cont

@app.route('/')
def home():

    return render_template('Home.html', Influenciadores = lista)

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html')

@app.route('/criar',methods = ['POST'])
def criar():
    global cont
    nome = request.form['nome']
    plataforma = request.form['plataforma']
    seguidores = request.form['seguidores']
    interesse = request.form['interesse']
    imagem = request.form['img']
    cont+=1
    obj = influencer(nome,plataforma,seguidores,interesse,imagem,cont)
    lista.append(obj)
    return redirect('/')

@app.route('/excluir/<idinf>',methods = ['GET','DELETE'])
def excluir(idinf):
    for i, p in enumerate(lista):
        if p.cont == int(idinf):
            lista.pop(i)
            break
    return redirect('/')

@app.route('/editar/<idinf>',methods = ['GET'])
def editar(idinf):
    for i, inf in enumerate(lista):
        if inf.cont == int(idinf):
            return render_template('Editar.html', influencer = inf, Titulo='Alterar Player')
@app.route('/alterar', methods = ['POST','PUT'])
def alterar():
    id = request.form ['id']
    for i, inf in enumerate(lista):
        if inf.cont == int(id):
            inf.nome = request.form['nome']
            inf.plataforma = request.form['plataforma']
            inf.seguidores = request.form['seguidores']
            inf.interesse = request.form['interesse']
            inf.imagem = request.form['img']
    return redirect('/')

lista = []
if __name__ == '__main__':
    app.run()
