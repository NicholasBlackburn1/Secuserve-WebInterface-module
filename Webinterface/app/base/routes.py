# -*- encoding: utf-8 -*-
"""
This is where I register all the webapps routs in the app
 TODO : add working and neet way of handling all the rounts needed for app
"""

import pathlib
from flask import jsonify, render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)
from turbo_flask import turbo
from turbo_flask.turbo import Turbo

from app import db, login_manager
from app.base import blueprint
from app.base.forms import AddFaceForm, LoginForm, CreateAccountForm, RemoveFaceForm
from app.base.models import User, Face

from app.base.util import verify_pass
from configparser import ConfigParser
import uuid

import pathlib
import app.base.const as const

from celery import Celery

from datetime import datetime
import calendar
# main web app entty point
@blueprint.route('/')
def route_default():
    return redirect(url_for('base_blueprint.login'))

## Login & Registration

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if 'login' in request.form:
        
        # read form data
        username = request.form['username']
        password = request.form['password']

        # Locate user
        user = User.query.filter_by(username=username).first()
        
        # Check the password
        if user and verify_pass( password, user.password):

            login_user(user)
            return redirect(url_for('base_blueprint.route_default',))

        # Something (user or pass) is not ok
        return render_template( 'accounts/login.html', msg='Wrong user or password', form=login_form)

    if not current_user.is_authenticated:
        return render_template( 'accounts/login.html',form=login_form)
    return redirect(url_for('home_blueprint.index'))




# this is the register roure for registering users to webpage
@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    login_form = LoginForm(request.form)
    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form:

        username  = request.form['username']
        email     = request.form['email'   ]

        # Check usename exists
        user = User.query.filter_by(username=username).first()
        if user:
            return render_template( 'accounts/register.html', 
                                    msg='Username already registered',
                                    success=False,
                                    form=create_account_form)

        # Check email exists
        user = User.query.filter_by(email=email).first()
        if user:
            return render_template( 'accounts/register.html', 
                                    msg='Email already registered', 
                                    success=False,
                                    form=create_account_form)

        # else we can create the user
        user = User(**request.form)
        db.session.add(user)
        db.session.commit()

        return render_template( 'accounts/register.html', 
                                msg='User created please <a href="/login">login</a>', 
                                success=True,
                                form=create_account_form)

    else:
        return render_template( 'accounts/register.html', form=create_account_form)


# logs out user from web app
@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('base_blueprint.login'))

## Errors

@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('page-403.html'), 403

@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('page-403.html'), 403

@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('page-404.html'), 404

@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('page-500.html'), 500


#TODO: get week and days linked up for displaying and manazging the display of total users seen fo that week
#TODO: pull from database per week entries for accuratly drawling what was seen on what weeks
@blueprint.route("/dashboard",methods=["GET", "POST"])
def display():
    day_of_month = datetime.now().day
    week_number = (day_of_month - 1) // 7 + 1
    monthnum= datetime.now().month
    month = calendar.month_name[monthnum]
    
    
    reconized= {'monday':1,'tuesday':2,'wensday':3,'thursday':4,'friday':5,'saturday':6,'sunday':10}
    unreconized= {'monday':10,'tuesday':20,'wensday':30,'thursday':40,'friday':50,'saturday':60,'sunday':43}

    face = Face.query.filter_by().all()
    for faces in face:
        
        const.name.append(str(faces.user))
        const.image.append(str(faces.image))
        
        
    
            
    return render_template("dash.html",seenreconized =reconized,seenunreconized=unreconized, week = week_number, month=month)

    
@blueprint.route("/settings",methods=["GET", "POST"])
def settings():
   
    remove_face= RemoveFaceForm(request.form)
    add_face =  AddFaceForm(request.form)
    if "add" in request.form:
       
        # read form data
        username = request.form["user"]
        group = request.form["group"]
        
        file = request.files["files"]
        imagename= request.files['files'].filename
        
        tempfile_path= str(pathlib.Path().absolute())+'/app/base/static/assets/tmp/'
        
        output_name = str(uuid.uuid1())+".jpg"
        
        tempfile_url = str('http://'+"192.168.5.8"+':'+"2000"+"/static/assets/tmp/"+output_name)
        
        phonenum = request.form["phone"]
        print(username)
        print(group)
        print(imagename)
        print(tempfile_url)
        print(phonenum)
        
        # saves uploaded image to a temp file dir for sending to opencv client 
        file.save(tempfile_path+output_name)

        # Check usename exists
        user = Face.query.filter_by(user=username).first()
       
        if user:
            return render_template(
                 "set.html",
                msg="Username already registered",
                add = add_face,
                remove = remove_face
              
            )
        if user == True:
             return render_template(
                 "set.html",
                msg="addeduser",
                add = add_face,
                remove = remove_face)
              

        # Check email exists
        user = Face.query.filter_by(group=group).first()
        
      
        user = Face.query.filter_by(image="none")
      
        
        
        user = Face(**request.form)
        user.image = output_name
        user.imageurl = tempfile_url
        user.useruuid = str(uuid.uuid4())
        user.phonenum = phonenum
        db.session.add(user)
        db.session.commit()
        ##print(image)

        
        return render_template("set.html",remove = remove_face,add= add_face, msg = "addeduser" )

    if "Remove" in request.form:
        username = request.form['user']
        group = request.form['group']

        print(username)
        print(group)

        remove = Face.query.filter_by(user=username).one()
        db.session.delete(remove)
        db.session.commit()
              
        return render_template("set.html",remove = remove_face,add= add_face, msg = "removedUser" )

    
    return render_template("set.html",remove = remove_face,add= add_face,msg = "None" )

  

def getFaceList(i):
    
    face=Face.query.filter_by().all()

    if(i > int(Face.query.filter_by().count())):
        const.name.append(str(face[i].user))
        const.image.append(str(face[i].image))
        i+=1
        return '{"names":}'
        