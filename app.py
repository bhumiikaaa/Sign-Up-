from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection details
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Your MySQL username
    password="bhumika@02",  # Your MySQL password
    database="university"  # Your MySQL database name
)

cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Insert student data into the database
        cursor.execute("INSERT INTO students (name, email, password) VALUES (%s, %s, %s)",
                       (name, email, password))
        db.commit()

        return redirect('/success')  # Redirect to a success page or homepage after insertion

    return render_template('signin.html')

@app.route('/success')
def success():
    return "Student successfully signed in!"

if __name__ == '__main__':
    app.run(debug=True)
