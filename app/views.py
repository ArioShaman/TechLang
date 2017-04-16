# -*- coding: utf-8 -*-
import os, re
import os.path
from app import app, db, lm
from flask import g,jsonify,request, render_template, Flask, url_for, flash, redirect,session, abort, session, send_from_directory,send_file
import models
from models import Admin,VocFolder,VocWord,Post, Message, RoomDialog, Videos, Events, Partipiant, Interests,UserInterest,check_unit_user
from app.forms import LoginForm, WordForm, FolderForm, Send
from flask.ext.login import login_user , logout_user , current_user , login_required
import datetime


@app.before_request
def before_request():
    g.admin = current_user


@app.route("/")
def hello():
	if 'loged_in' in session:
		uslname = True
		curname = session['nickname']
		town = session.get('town')
	else:
		uslname = False
		curname = 'Guest'
		town = ''
	return render_template('index.html',uslname = uslname,curname = curname,town = town)

@app.route('/vocabulary')
def vocabulary():
	if 'loged_in' in session:
		uslname = True
		curname = session['nickname']
		town = session.get('town')
		autor= session.get('nickname')
		folders = VocFolder.query.filter_by(autor=autor).all()
		return render_template('vocabulary.html',uslname = uslname,curname = curname,town = town, folders = folders)
	else:
		return render_template('plreg.html')

	#return render_template('vocabulary.html',uslname = uslname,curname = curname,town = town)

@app.route('/folder/<id_folder>')
def words(id_folder):
	if 'loged_in' in session:
		session['id_folder'] = id_folder
		uslname = True
		curname = session['nickname']
		town = session.get('town')
		autor= session.get('nickname')
		words = VocWord.query.filter_by(folder_id=id_folder).all()
		return render_template('words.html',uslname = uslname,curname = curname,town = town, words=words)
	else:
		return render_template('plreg.html')

	#return render_template('vocabulary.html',uslname = uslname,curname = curname,town = town)

@lm.user_loader
def load_user(id):
    return Admin.query.get(int(id))


@app.route('/login_page')
def login_page():
	if 'loged_in' in session:
		uslname = True
		curname = session['nickname']
		town = session.get('town')
	else:
		uslname = False
		curname = 'Guest'
		town = ''
	form = LoginForm()
	return render_template('login.html',form = form,uslname = uslname,curname = curname,town = town)

@app.route('/logout')
def logout():
    logout_user()
    session.pop('loged_in', None)
    session.pop('nickname',None)
    session.pop('password', None)
    return redirect('/') 

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'GET':
		form = LoginForm()
		return render_template('login.html',form = form)
	nickname = request.form['nickname']
	password = request.form['password']
	auth_user = Admin.query.filter_by(nickname=nickname).first()
	if auth_user is None:
		form = LoginForm()
		return render_template('login.html', form=form)
	if password != Admin.query.filter_by(nickname=nickname).first().password:
		form = LoginForm()

		return render_template('login.html', form=form)
	login_user(auth_user)
	current_user = Admin.query.filter_by(nickname=nickname).first().nickname
	session['nickname'] = nickname
	session['town'] = Admin.query.filter_by(nickname=nickname).first().town
	session['loged_in'] = True
	return redirect('/') 


@app.route('/register',methods=['GET','POST'])
def register():
	return redirect('/')




@app.route('/test')
def tester():
	autor= session.get('nickname')
	passw = 'test'
	return render_template('test.html',passw= passw, autor = autor)


@app.route('/add_folder')
def add_folder():
	form = FolderForm()
	return render_template('addfold.html', form = form)

@app.route('/add_word')
def add_word():
	form = WordForm()
	return render_template('addword.html',form = form)

@app.route('/addfold',methods=['GET','POST'])
def addfold():
	if request.method == 'GET':
		form = FolderForm()
		return render_template('addfold.html',form = form)
	name = request.form['name_folder']

	autor = session.get('nickname')
	folder = VocFolder(autor = autor, name_folder = name)
	db.session.add(folder)
	db.session.commit()
	return redirect('/vocabulary')
	#return render_template('test.html',folder = folder, autor = autor)

@app.route('/addword',methods=['GET','POST'])
def addword():
	if request.method == 'GET':
		form = WordForm()
		return render_template('addword.html',form = form)
	else:
		eng = request.form['eng']
		rus = request.form['rus']
		desc = request.form['desc']
		cover = request.form['cover']
		id_fold = session.get('id_folder')
		word = VocWord(folder_id = id_fold, eng = eng, rus = rus, desc =desc,link_cover=cover)
		db.session.add(word)
		db.session.commit()
		return redirect('/vocabulary')


def dia_name(u_id):
	name = Admin.query.filter_by(uid=u_id).first().nickname
	return name

def oportunete_name(u_id):
	nickname = session.get('nickname')
	r_id = RoomDialog.query.filter_by(user_id = u_id).first().r_id
	rooms = RoomDialog.query.filter_by(r_id =r_id).all()
	for room in rooms:
		u_id = room.user_id
		user = Admin.query.filter_by(uid = u_id).first()
		if user.nickname != nickname:
			cur_u = user.nickname
	return cur_u
def get_name(uid):
	l_name = Admin.query.filter_by(uid = uid).first().Lastname
	f_name = Admin.query.filter_by(uid = uid).first().Firstname
	return str(l_name)+"  "+str(f_name)

def get_lname(nickname):
	l_name = Admin.query.filter_by(uid = uid).first().Lastname
	f_name = Admin.query.filter_by(uid = uid).first().Firstname
	return str(l_name)+"  "+str(f_name)

def my(uid):
	message_aut_id = Message.query.filter_by(uid = uid).first().autor_id
	message_aut = Admin.query.filter_by(uid = message_aut_id).first().nickname
	nickname = session.get('nickname')
	
	if nickname == message_aut:
		return True
	else:
		return False
	

@app.route('/dialogs')
def getchat():
	if 'loged_in' in session:
		uslname = True
		curname = session['nickname']
		town = session.get('town')
		form = Send()
		nickname = session.get('nickname')
		user_id = Admin.query.filter_by(nickname = nickname).first().uid
		r_id = RoomDialog.query.filter_by(user_id = user_id).first().r_id
		dialogs = RoomDialog.query.filter_by(r_id = r_id).all()
		return render_template('chat.html',form = form,dia_name =dia_name,uslname = uslname, curname = curname,town = town, dialogs = dialogs,user_id = user_id)
	else:
		uslname = False
		curname = 'Guest'
		town = ''
		form = Send()
	return render_template('chat.html',form = form,
		uslname = uslname,curname = curname,
		town = town
	)

def last_element(r_id):
	List = Message.query.filter_by(room_id = r_id).all()
	#l = len(List)
	last_mes = List[-1]
	last_mes = last_mes.uid
	return last_mes


@app.route('/im/<r_id>')
def concret_chat_root(r_id):
	if 'loged_in' in session:
		uslname = True
		curname = session['nickname']
		town = session.get('town')
		form = Send()
		nickname = session.get('nickname')
		user_id = Admin.query.filter_by(nickname = nickname).first().uid
		dialogs = RoomDialog.query.filter_by(r_id = r_id).all()
		messages = Message.query.filter_by(room_id = r_id).all()
		session['room_id'] = r_id

		return render_template('curr_chat.html',
			form = form,dia_name =dia_name,
			oportunete_name=oportunete_name,
			last_element = last_element,
			messages=messages,uslname = uslname,
			curname = curname,town = town,
			dialogs = dialogs,user_id = user_id,
			get_name = get_name,
			my = my,
			r_id = r_id
		)
	else:
		uslname = False
		curname = 'Guest'
		town = ''
		form = Send()
		return render_template('chat.html',form = form,uslname = uslname,curname = curname,town = town)


@app.route('/post/<uid>')
def req_post(uid):
	if 'loged_in' in session:
		uslname = True
		curname = session['nickname']
		town = session.get('town')
		post_id = uid
		post = Post.query.filter_by(uid = post_id).first()
		return render_template('post.html',
			post = post,uslname = uslname,
			curname = curname,town = town,
			get_art = get_art)
	else:
		return render_template('plreg.html')



@app.route('/send_mess/<r_id>/<user_id>',methods=['GET','POST'])
def send_message(r_id,user_id):
	if request.method == 'GET':
		form = WordForm()
		return redirect('/dialogs')
	else:
		message_text = request.form['message']
		message = Message(room_id=r_id,
			autor_id = user_id,
			message = message_text,
		)
		session['room_id'] = r_id
		db.session.add(message)
		db.session.commit()
		return redirect('/im/%s'%(r_id))

@app.route('/cources/<nickname>')
def cources(nickname):
	if 'loged_in' in session:
		uslname = True
		curname = session['nickname']
		town = session.get('town')
		uid = Admin.query.filter_by(nickname=nickname).first().uid
		videos = Videos.query.filter_by(user_id = uid).all()
		posts = Post.query.filter_by(autor=nickname).order_by('uid desc').all()
		nickname = nickname
		return render_template('account-teacher.html',posts = posts,videos = videos,
			uslname = uslname,curname = curname,
			town = town, nickname = nickname)
	else:
		return render_template('plreg.html')

@app.route('/search')
def search():
	if 'loged_in' in session:
		uslname = True
		curname = session['nickname']
		town = session.get('town')
		uid = Admin.query.filter_by(nickname=curname).first().uid
		return render_template('search.html',uslname = uslname,curname = curname,town = town)
	else:
		return render_template('plreg.html')

@app.route('/units')
def get_units():
	if 'loged_in' in session:
		uslname = True
		curname = session['nickname']
		town = session.get('town')
		uid = Admin.query.filter_by(nickname=curname).first().uid
		last_check_unit = check_unit_user.query.filter_by(user_id = uid).first().check_unit
		if last_check_unit == None:
			return redirect('/unit/1')
		else:
			return redirect('unit/%s'%(last_check_unit))
			#return render_template('test.html', last =last_check_unit)

		return render_template('units.html',uslname = uslname,
			curname = curname,town = town,
			last = last_check_unit,
			)
	else:
		return render_template('plreg.html')

@app.route('/unit/<index>')
def get_unit(index):
	if 'loged_in' in session:
		uslname = True
		curname = session['nickname']
		town = session.get('town')
		uid = Admin.query.filter_by(nickname=curname).first().uid
		return render_template('unit%s.html'%index,uslname = uslname,
			curname = curname,town = town
			)
	else:
		return render_template('plreg.html')

@app.route('/publicate')
def publicater():
	if 'loged_in' in session:
		uslname = True
		curname = session['nickname']
		town = session.get('town')
		uid = Admin.query.filter_by(nickname=curname).first().uid
		return render_template('post_form.html',uslname = uslname,
			curname = curname,town = town
		)
	else:
		return render_template('plreg.html')


def write_file(post_id,data):
	basedir = os.path.abspath(os.path.dirname(__file__))
	f = open('%s/templates/posts/post%s.html'%(basedir,post_id),'w')
	f.write(data)
	f.close()

def get_art(post_id):
	basedir = os.path.abspath(os.path.dirname(__file__))
	f = open('%s/templates/posts/post%s.html'%(basedir,post_id),'r')
	data = f.read()
	return data

@app.route('/publish',methods=['GET','POST'])
def publish():
	if 'loged_in' in session:
		uslname = True
		curname = session['nickname']
		town = session.get('town')
		uid = Admin.query.filter_by(nickname=curname).first().uid
		title = request.args.get('title')
		desk = request.args.get('descript')
		cover = request.args.get('coverlink')
		data = request.args.get('editor1')

		autor = Post(autor = curname,title = title,desk = desk,
			cover = cover)#,article = data)
		p_id = get_last_post()
		p_id = int(p_id) +1
		write_file(p_id,data)
		db.session.add(autor)
		db.session.commit()
		return redirect('/cources/%s'%curname)
	else:
		return render_template('plreg.html')

@app.route('/id')
def get_profile():
	return render_template('profile.html')

def get_last_post():		
	uid = Post.query.all()
	uid = str(uid[-1].uid)
	return uid