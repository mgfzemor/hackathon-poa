from flask import Flask, render_template,request,jsonify
from cadastro import *

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('index.html')

@app.route('/cadastro',methods=['GET', 'POST'])
def cadastro():
    mail = request.form['mail']
    passwd = request.form['passwd']
    user = request.form['user']
    out = cadastro_usuario(mail,passwd,user)
    return render_template('main.html')

@app.route('/estados')
def est():
    return render_template('estados.html')

@app.route('/pesquisar')
def pesquisa():
    a = request.args.get('a')
    print 'entrou flask',a
    out = search_trie(a,trie_school)
    if out:
        out = search_school_list(out)
    else:
        out = [-1,'Not Found... =|']
    return jsonify(result=out)

@app.route('/busca')
def busca():
    return render_template('busca.html')

@app.route('/cidades')
def busca_cidade():
    return render_template('busca_cidade.html')


@app.route('/aluno',methods=['GET', 'POST'])
def aluno():
    num = request.form['num']
    if num:
        out =make_page_aluno(num)
        found = out[0]
        aluno = out[1]
        escola = out[2]
        rank_escola = out[3]
        graph_notas = out[4]
        rank_cidade = out[5]
        #====== Municipio data ==============
        out_mun = busca_mun(aluno.cod_municipio)
        municipio = out_mun[0]
        return render_template('aluno.html',aluno=aluno,found=found,escola=escola,rank_escola=rank_escola,graph_notas=graph_notas,municipio=municipio,rank_cidade=rank_cidade)
    else:
        return render_template('aluno.html',aluno=aluno,found=found,escola=escola,lista_pos=lista_pos,graph_notas=graph_notas)

if __name__ == '__main__':
    app.run()
