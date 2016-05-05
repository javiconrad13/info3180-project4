from app import app,db
from flask import Flask, abort, request, jsonify, g, url_for, render_template,session
import requests
from image_getter import image_dem
from models import User,Wishlist, Token
import json

@app.route('/')
def home():
    return app.send_static_file("home.html")

@app.route('/api/user/register', methods=['POST','GET'])
def register():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        new_user=User(email=email,name=name,password=password)
        db.session.add(new_user)
        db.session.commit()
        hold={'error':'null','data':{'token':'blank','expires':'time','user':{'id':new_user.get_id(),'email':new_user.email,'name':new_user.name},},'message':'Registration Successful'}
        return jsonify(hold)
    return render_template("register.html")

@app.route('/api/user/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        user=User.query.filter(User.email==email).first()
        if not user:
            hold={'error':'1','data':{},'message':'Incorrect, Please re-enter username and password'}
            return jsonify(hold)
        if password==user.password:
            hold={'error':'null','data':{'token':'blank for now','expires':'time','user':{'id':user.user_id,'email':user.email,'name':user.name},},'message':'Login Successful'}
            return jsonify(hold)
        else:
            hold={'error':'1','data':{},'Incorrect, Please re-enter username and password'}
            return jsonify(hold)

    return jsonify({'result':'page loaded'});   

@app.route('/api/user/logout')
def logout():
    session.pop('logged_in', None)
    return jsonify({'result': 'Logged Out'})
    
@app.route('/api/user/<int:id>/wishlist',methods=['POST','GET'])
def wishlist(id):
    if request.method=='POST':
        title=request.form['title']
        description=request.form['description']
        url=request.form['url']
        thumbnail=request.form['thumbnail']
        hold={'error':'null','data':{'wishes':{'title':title,'description':description,'url':url,'thumbnail':thumbnail},'message':'Successfully added'},}
        new_wishlist=Wishlist(title,description,url,thumbnail,id)
        db.session.add(new_wishlist)
        db.session.commit()
        return jsonify(hold)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8080)