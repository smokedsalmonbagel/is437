from flask import Flask
from flask import render_template
from flask import request,session, redirect, url_for, escape,send_from_directory,make_response 
from flask_session import Session
from datetime import timedelta

app = Flask(__name__,static_url_path='')

app.config['SECRET_KEY'] = '#$%34563453563$%$'
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=5)
sess = Session()
sess.init_app(app)

@app.route('/')
def home():
    return 'homepage'
    
    
@app.route('/selectProd',methods=['GET','POST'])
def selectProd():
    return render_template('selectProd.html')
    
@app.route('/selectShip',methods=['GET','POST'])
def selectShip():
    product = request.form.get('product')
    session['product'] = product
    return render_template('selectShip.html',product=product)
    
@app.route('/confirm',methods=['GET','POST'])
def confirm():
    #product = request.form.get('product')
    product = session['product']
    ship = request.form.get('ship')
    return render_template('confirm.html',product=product,ship=ship)
    
    
    
    
@app.route('/set')
def set():
    session['key'] = 'value'
    return 'ok'

@app.route('/get')
def get():
    return session.get('key', 'not set')
    
@app.route('/test')
def test():
    user = 'Tommy'
    return render_template('test.html',username = user)

#display form   
@app.route('/enterName')
def enterName():
    return render_template('nameForm.html')

#process form   
@app.route('/submitName',methods=['GET','POST'])
def submitName():
    username = request.form.get('myname')
    othername = request.form.get('othername')
    print(othername)
    print(username)
    #At this point we would INSERT the user's name to the mysql table
    return render_template('message.html',msg='name '+str(username)+' added!')


@app.route('/submitNameGet',methods=['GET','POST'])
def submitNameGet():
    username = request.args.get('myname')
    print(username)
    #At this point we would INSERT the user's name to the mysql table
    return render_template('message.html',msg='name '+str(username)+' added!')

@app.route('/elements')
def elements():
    return render_template('formelements.html')



@app.route('/register')
def register():
    account = 'jan@aol.com'
    return render_template('myregistration.html',account = user_account)



# endpoint route for static files
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
    
    
    
    
  
if __name__ == '__main__':
   app.run(host='127.0.0.1',debug=True)   