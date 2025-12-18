from flask import Flask,render_template,request,flash,redirect,url_for
from models import db,User,Task
from flask_bcrypt import Bcrypt
from flask_login import LoginManager,login_user,login_required,logout_user,current_user
from datetime import datetime

app = Flask(__name__)
app.secret_key='secret'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:root@localhost:3306/todo'
db.init_app(app)
bcrypt = Bcrypt(app)
#creating object for login restricing the user to not to navigate without login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get_or_404(user_id)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('username','')
        email = request.form.get('useremail','')
        password = request.form.get('userpassword','')
        check_email = User.query.filter_by(email=email).first()
        if check_email:
            return render_template('login.html',message='This email is already registered')
        else:
            #left side name or variable is from model that is from Db and right side variable is from form that is above this
            user = User(name=name,email=email,password=bcrypt.generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            flash('Account Created Successfully')
            return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/login/', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('useremail','')
        password = request.form.get('userpassword')
        user = User.query.filter_by(email=email).first()
        if user:
            if bcrypt.check_password_hash(user.password,password):
                login_user(user)
                flash('You were successfully logged in')
                return redirect(url_for('dashboard'))
            else:
                flash('You have entered the incorrect password')
                return redirect(url_for('login'))
        else:
            flash('You are not registered, please create a account')
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/dashboard/', methods = ['GET','POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        task_name = request.form.get('task_name','')
        task_desc = request.form.get('task_desc','')
        comp_date = request.form.get('comp_date','')
        prio = request.form.get('prio','')
        cato = request.form.get('cato','')
        task = Task()
        task.task_name = task_name
        task.task_desc = task_desc
        task.comp_date = comp_date
        if prio:
            task.priority = prio
        if cato:
            task.cato = cato
        task.rel_user = current_user.id
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('dashboard'))
    task = Task.query.filter_by(rel_user=current_user.id).all()
    date_time = datetime.now()
    dt = date_time.strftime("%d-%m-%Y %H:%M:%S")
    return render_template('dashboard.html', today_date=dt,task=task)


@app.route('/profile/')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('login'))