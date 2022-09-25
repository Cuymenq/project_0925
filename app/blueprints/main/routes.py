from . import bp as app
from flask import render_template, request, redirect, url_for, flash
from app.blueprints.main.models import User, Pokemon
from app import db
from flask_login import current_user, login_required

# Routes that return/display HTML

@app.route('/')
@login_required
def home():
    posts = Pokemon.query.all()

    return render_template('home.html', user=current_user, posts=posts)


@app.route('/pokemons')
def pokemons():
    pass



@app.route('/pokemon', methods=['POST'])
@login_required
def create_post():
    poke_name = request.form['name']
    poke_desc = request.form['description']
    
    new_pokemon = Pokemon(name=poke_name, description=poke_desc, user_id=current_user.id)

    db.session.add(new_pokemon)
    db.session.commit()

    flash('Post added successfully', 'success')
    return redirect(url_for('main.home'))

@app.route('/pokemon/<id>')
def post(id):
    single_post = Pokemon.query.get(id)
    return render_template('Caught.html', post=single_post)