from app import app, db
from flask import render_template, redirect, url_for, request, flash, session, g, jsonify, json
from forms import Form
from models import Country, State, City



@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()
    form.country.choices = [(country.id, country.name) for country in Country.query.all()]
  
    if request.method == 'POST':
       city = City.query.filter_by(id=form.city.data).first()
       country = Country.query.filter_by(id=form.country.data).first()
       state = State.query.filter_by(id=form.state.data).first()
       return '<h1>Country : {}, State: {}, City: {}</h1>'.format(country.name, state.name, city.name)
    return render_template('index.html', form=form)
 
@app.route('/state/<get_state>')
def statebycountry(get_state):
    state = State.query.filter_by(country_id=get_state).all()
    stateArray = []
    for city in state:
        stateObj = {}
        stateObj['id'] = city.id
        stateObj['name'] = city.name
        stateArray.append(stateObj)
    return jsonify({'statecountry' : stateArray})
  
@app.route('/city/<get_city>')
def city(get_city):
    state_data = City.query.filter_by(stateid=get_city).all()
    cityArray = []
    for city in state_data:
        cityObj = {}
        cityObj['id'] = city.id
        cityObj['name'] = city.name
        cityArray.append(cityObj)
    return jsonify({'citylist' : cityArray}) 



