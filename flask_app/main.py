from flask import Flask
from flask import render_template
from flask import request,session, redirect, url_for, escape,send_from_directory,make_response 

app = Flask(__name__,static_url_path='')

@app.route('/')
def home():
    return 'homepage'
    
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