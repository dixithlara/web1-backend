from flask import Blueprint,render_template,request,flash

auth=Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    return "<p>Login</p>"

@auth.route('/logout/')
def logout():
    return "<p>Logout</p>"

@auth.route('/signup',methods=['GETS','POSTS'])
def signup():
    if request.method=='POST':
        email=request.form.get('email')
        firstName=request.form.get('firstname')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        
        if len(email)<3:
            flash('email must be atleast 2 characters.',category='error') 
        elif len(firstName<2):
            flash('first name must be atlest 1 charater.',category='error')
        elif password1!=password2:
            flash('password is not macthing.',category='error')
        elif len(password1)<7:
            flash('password must be atleast 7 characters.',category='error')
        else :
            #allow user
            flash('Account created!',category='success')


    return render_template("signup.html") 
