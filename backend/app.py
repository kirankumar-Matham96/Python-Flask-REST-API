from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
CORS(app) # enables cors for all routes
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def json(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}
with app.app_context():
    db.create_all()

#create a test rout
@app.route("/test", methods=['GET'])
def test():
    return make_response(jsonify({'message': 'The server is running'}), 200)

# create new user
@app.route('/api/flask/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()

        required_fields = ['name', 'email']
        for field in required_fields:
            if field not in data:
                return make_response(jsonify({'message': f'Missing {field}'}), 400)

        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()

        return make_response(jsonify({
            'id': new_user.id,
            'name': new_user.name,
            'email':new_user.email
        }), 201)
    
    except Exception as e:
        return make_response(jsonify({'message': "Error creating user", 'error': str(e)}), 500)

# get all the users
@app.route("/api/flask/users", methods=['GET'])
def get_all_users():
    try:
        users = User.query.all()
        # users_data = [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]
        users_data = [user.json() for user in users]
        return make_response(jsonify(users_data), 200)
    
    except Exception as e:
        return make_response(jsonify({'message': 'error getting all the users', 'error': str(e)}), 500)

# get user by id
@app.route("/api/flask/users/<id>", methods=['GET'])
def get_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            return make_response(jsonify({'user': user.json()}),200)
        return make_response(jsonify({'message': 'user not found'}),404)
    
    except Exception as e:
        return make_response(jsonify({'message': 'error getting all the users', 'error': str(e)}), 500)

# update user
@app.route("/api/flask/users/<id>", methods=['PUT'])
def update_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.name = data['name']
            user.email = data['email']
            db.session.commit()
            return make_response(jsonify({'message': 'user updated'}), 200)        
        return make_response(jsonify({'message': 'user not found'}), 404)

    except Exception as e:
        return make_response(jsonify({'message': 'error getting all the users', 'error': str(e)}), 500)

# delete user
@app.route("/api/flask/users/<id>", methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({'message': 'user deleted'}),200)
        return make_response(jsonify({'message': 'user not found'}),404)
     
    except Exception as e:
        return make_response(jsonify({'message': 'error getting all the users', 'error': str(e)}), 500)

