from flask import render_template
from flask.helpers import flash
from flask_login.utils import login_required
from flask import redirect
from app import app
from app.forms import LoginForm, SignupForm
from app.models import User
from app import db
from flask_login import login_user, current_user, logout_user
from flask import request
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    users =[ 
            {'id':'id01','name':'Duyratdz','age':'19'},
            {'id':'id02','name':'Duy','age':'19'},
            {'id':'id03','name':'Duydz','age':'19'}
          ] 
    return render_template('index.html', title='My title',users=users)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Kiem tra user (current_user) da duoc xac thuc hay chua
    if current_user.is_authenticated:
        return redirect('/index')
        
    # LOI!!!
    form = LoginForm()
    
    # Nguoi dung co nhap du lieu
    if form.validate_on_submit():
        # Kiem tra username tu form trung voi username trong DB
        user = User.query.filter_by(username=form.username.data).first()
        # Kiem tra password
        if user:
            # Kiem tra user.password co trung voi form.password.data hay ko
            pass_ok = (user.password==form.password.data)
        if user is None or not pass_ok:
            flash('Invalid username or password')
            return redirect('/login')

        flash('Login of user {}'.format(form.username.data))
        login_user(user)
        #Thong tin của trang tiep theo 
        next_page = request.args.get('next')
        if next_page is None:
            next_page = 'index'
        else: 
            flash('Next page is: '+next_page)
              # Xu ly gia tri next la dia chi web
            if url_parse(next_page).netloc != '':
                flash('netloc: ' + url_parse(next_page).netloc)
                next_page = '/index'
        return redirect(next_page)
    return render_template('login.html', title='Sign in', form=form)

@app.route('/signup', methods = ['GET','POST'])
def signup():
     #kiem tra user(current_user) da dc xac thuc hay chua
    if current_user.is_authenticated:
      return redirect('/index')
    form = SignupForm()
    # nguoi dung co nhap du lieu:
    if form.validate_on_submit():
        #kiem tra password
        if (form.password.data != form.repassword.data):
            flash('repassword is not correct')
            return redirect('/signup')         
        if User.query.filter_by(username=form.username.data).first() is not None :
            flash('username is exist')
            return redirect('/signup')
        u1=User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(u1)
        db.session.commit()
        flash(f'Signup of user {form.username.data}')
        login_user(u1)
        return redirect('/signup')       
    return render_template('signup.html', title='Sign up', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('index')

@app.route('/upload')
def upload():
    return render_template('upload.html')