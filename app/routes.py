from flask import render_template, flash, redirect
from flask import request, jsonify
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'dproffit1'}
    classes = [{'classInfo': {'code': 'CSC324', 'title': 'DevOps'}, 'instructor': 'Baoqiang Yan'},
               {'classInfo': {'code': 'CSC374', 'title': 'Unix/Linux Systems Admin'}, 'instructor': 'Greg Lawson'},
               {'classInfo': {'code': 'CSC305', 'title': 'Database Architecture'}, 'instructor': 'Devon Muse'},
               {'classInfo': {'code': 'SEC425', 'title': 'Ethical Hacking'}, 'instructor': 'Frank Luzsicza'},]
    return render_template('index.html', title='Home', user=user, classes=classes)

@app.route('/dproffit1')
def dproffit1():
	return render_template('dproffit1.html', title='YAY!')

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			flash('Welcome user {}! You opted for remember_me={}'.format(form.username.data, form.remember_me.data))
			return redirect('/dproffit1')
	else:
		if request.args:
			flash('GET method now allowed for login!')        # else:        #     flash('No data in request!')
	return render_template('Login.html', title='Sign In', form=form)

@app.route('/json')
def jsonTest():
	# return jsonify(list(range(5)))
	instructor = {
	"username": "byan",
	"role": "instructor",
	"uid": 11,
	"name":{
		"firstname": "Baoqiang",
		"lastname": "Yan"
		}
	}
	return jsonify(instructor)
