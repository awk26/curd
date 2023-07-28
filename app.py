from flask import *
from dbm2 import *

app=Flask(__name__)
@app.route("/")
def index():
    return render_template('login.html')
@app.route('/register')
def reg():
    return render_template('register.html')
@app.route('/login_validation', methods=['POST'])
def  login_validation():
    email=request.form.get('email')
    password=request.form.get('password')
    t=(email,password)
    t1=select()
    if t in t1:
        return redirect('/home')
    else:
        return   redirect('/')  

@app.route('/add_user',methods=['POST'])
def add_user():

    name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    t=(name,email,password)
    insert(t)
    return redirect('/')

@app.route("/hm")
def hom():
    return render_template("home.html")

@app.route('/home')
def home():
    data=select1()
    return render_template("home.html",t=data)
    
    #return redirect("/hm")
@app.route("/dele/<int:id>', methods=['POST'])")
def dele(id):

    delete(id)
    return redirect("/home")    

@app.route('/update_user/<int:id>', methods=['POST'])
def update_user(id):
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    t=(name,email,password,id)
    update(t)
    data=select1()
    return render_template("register.html",t=data)
      



if __name__=="__main__": 
    app.run(debug=True)   

