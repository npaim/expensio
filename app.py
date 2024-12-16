from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app
app = Flask(__name__)

# Set up PostgreSQL database URI (replace with your credentials)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Noander!123@localhost:5432/expensio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoid overhead
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    __tablename__ = 'users'  # Ensure this matches your table name in PostgreSQL
    __table_args__ = {'schema': 'expensio'}  # Specify the schema name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

# Define a route to get all users
@app.route('/users/all', methods=['GET'])
def get_users():
    try:
        # Query all users from the users table
        users = User.query.all()

        # Convert result to a list of dictionaries
        users_data = [{"id": user.id, "name": user.name, "age": user.age} for user in users]
        return jsonify(users_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
