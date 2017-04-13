from flask_wtf import Form 
from wtforms import Form, BooleanField, StringField, PasswordField,TextField,FileField, validators
from app.models import Admin
from flask_wtf.file import FileField, FileAllowed, FileRequired
#from flask_uploads import UploadSet, IMAGES



class LoginForm(Form):
	nickname = StringField('Username',[validators.Required()],render_kw={"placeholder": "Enter your username"})
	password = PasswordField('Password',[validators.Required()],render_kw={"placeholder": "Enter your password"})
 

class WordForm(Form):
	eng = StringField('English',[validators.Required()],render_kw={"placeholder": "Enter english"})
	rus = StringField('Russian',[validators.Required()],render_kw={"placeholder": "Enter russian"})
	desc = StringField('Description',[validators.Required()],render_kw={"placeholder": "Enter description"})
	cover = StringField('Link to cover',[validators.Required()],render_kw={"placeholder": "Enter link for your image"})
    
   
class FolderForm(Form):
	name_folder = StringField('Russian',[validators.Required()],render_kw={"placeholder": "Enter folder name"})

class Send(Form):
	#message = TextField('Message',[validators.Length(min=1, max=564)],render_kw={"placeholder": "Enter message"})
	message = TextField('Message',[validators.Required()],render_kw={"placeholder": "Enter message"})