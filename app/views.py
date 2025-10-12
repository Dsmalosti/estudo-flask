from app import app, db
from flask import render_template, request, url_for, redirect

from app.models import Contato
from app.forms import ContatoForm

@app.route('/')
def homepage():
    usuario = 'Diogo'
    idade = 21
    context = {
        'usuario': usuario,
        'idade': idade
    }
    return render_template('index.html', context=context)


@app.route('/contato/', methods=['GET', 'POST'])
def contato():
    form = ContatoForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
    
    return render_template('contato.html', context=context, form=form)


@app.route('/contato/lista/')
def contatoLista():     

    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')
    

    dados = Contato.query.order_by('nome')
    if pesquisa != '':
        dados = dados.filter_by(nome=pesquisa)

    print(dados)

    context = {'dados': dados.all()}

    return render_template('contato_lista.html', context=context)


@app.route('/contato/<int:id>/')
def contatoDetail(id):
    obj = Contato.query.get(id)
    

    return render_template('contato_detail.html', obj=obj)