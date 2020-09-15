from datetime import datetime
from flaskblog import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"


# step: 1 : after create the database models  --> goto python shell
#           >>> from flaskblog import db      --> from (app file_name) import db
# step: 2 : create the db file enter-->
#           >>> db.create_all()
#           site.db file will appear in the project directory
# step: 3 : import models from flaskblog(app file)
#           >>> from flaskblog import User, Post
# step: 4 : create user
#           >>> user_hari = User(username='Hari',email='haridemo@gmail.com',password='password')
# step: 5 : add user
#           >>> db.session.add(user_hari)
# step: 6 : Commit
#           >>> db.session.commit()
#         query methods:
#        ----------------
# Find list of users
#           >>> User.query.all()
# If select the first user
#           >>> User.query.first()
# If use filter_by method for perticular selection
#           >>> User.query.filter_by(username='Hari').all()
# If use filter_by method for perticular first selection
#           >>> User.query.filter_by(username='Hari').first()
# >>> User.query.filter_by(username='Hari').first()
# User('Hari','haridemo@gmail.com','default.jpg')
# >>> user = User.query.filter_by(username='Hari').first()
# >>> user
# User('Hari','haridemo@gmail.com','default.jpg')
# >>> user.id
# 1
# >>> user = User.query.get(1)
# >>> user
# User('Hari','haridemo@gmail.com','default.jpg')
# >>> user.posts
# []
# >>> db.drop.all() --> drop all database tables & rows
# >>> db.create_all() --> to create tables and rows
# >>> User.query.all()
# []
# >>> Post.query.all()
# []
"""
Microsoft Windows [Version 10.0.18362.1082]
(c) 2019 Microsoft Corporation. All rights reserved.

(venv) F:\Data Science\PYTHON\Flask_Projects>python
Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> db.session.commit()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'db' is not defined
>>> exit()

(venv) F:\Data Science\PYTHON\Flask_Projects>cd blog_project

(venv) F:\Data Science\PYTHON\Flask_Projects\Blog_project>python
Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> db.session.commit()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'db' is not defined
>>> user.id
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'user' is not defined
>>> User.query.all()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'User' is not defined
>>> from flaskblog import db
F:\Data Science\PYTHON\Flask_Projects\venv\lib\site-packages\flask_sqlalchemy\__init__.py:833: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be
disabled by default in the future.  Set it to True or False to suppress this warning.
  warnings.warn(FSADeprecationWarning(
>>> User.id
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'User' is not defined
>>> user.id
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'user' is not defined
>>> db.create_all()
>>> from flaskblog import User, Post
>>> db.session.add(user_hari)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'user_hari' is not defined
>>> user_hari = User(username='Hari',email='hari@gmail.com',password='password')
>>> user_harikrishna = User(username='Harikrishna',email='harikrishna@gmail.com',password='password')
>>> db.session.commit()
>>> User.query.all()
[User('Hari','haridemo@gmail.com','default.jpg'), User('Krishna','krishnademo@gmail.com','default.jpg')]
>>> User.query.first()
User('Hari','haridemo@gmail.com','default.jpg')
>>> User.query.filter_by(username='Hari').all()
[User('Hari','haridemo@gmail.com','default.jpg')]
>>> User.query.filter_by(username='Hari').first()
User('Hari','haridemo@gmail.com','default.jpg')
>>> user.id
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'user' is not defined
>>> user=User.query.filter_by(username='Hari').first()
>>> user.id
1
>>> user=User.query.get(1)
>>> user
User('Hari','haridemo@gmail.com','default.jpg')
>>> user.posts
[]
>>> post_1 = Post(title='Blog 1',content='First post content',user_id=user_id)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'user_id' is not defined
>>> post_1 = Post(title='Blog 1',content='First post content',user_id=user_id)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'user_id' is not defined
>>> post_1 = Post(title='Blog 1',content='First post content',user_id=user.id)
>>> post_2 = Post(title='Blog 2',content='Second post content!',user_id=user.id)
>>> db.session.add(post_1)
>>> db.session.add(post_21)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'post_21' is not defined
>>> db.session.add(post_2)
>>> db.session.commit()
>>> user.post
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'User' object has no attribute 'post'
>>> user.posts
[Post('Blog 1','2020-09-15 09:28:41.469935'), Post('Blog 2','2020-09-15 09:28:41.471931')]
>>> for post in posts:
... print(post)
  File "<stdin>", line 2
    print(post)
    ^
IndentationError: expected an indented block
>>> print(post.title)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'post' is not defined
>>> for post in posts:
... print(post.title)
  File "<stdin>", line 2
    print(post.title)
    ^
IndentationError: expected an indented block
>>> for post in posts:
... ... print(post.title)
  File "<stdin>", line 2
    ... print(post.title)
    ^
IndentationError: expected an indented block
>>> for post in posts:
...     print(post.title)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'posts' is not defined
>>> user.posts
[Post('Blog 1','2020-09-15 09:28:41.469935'), Post('Blog 2','2020-09-15 09:28:41.471931')]
>>> for post in user.posts:
...     print(post.title)
...
Blog 1
Blog 2
>>> post = post.query.first()
>>> post
Post('Blog 1','2020-09-15 09:28:41.469935')
>>> post.user_id
1

"""