from flask import Flask , redirect, url_for, render_template, request

import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('movie.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Movies (id INTEGER PRIMARY KEY AUTOINCREMENT,name text NOT NULL,actor text NOT NULL,actress text NOT NULL,director text NOT NULL,year text NOT NULL);")
#print("db created")
conn.commit()
conn.close()



@app.route('/')
def hello_world():  # put application's code here
    conn1 = sqlite3.connect('movie.db')
    c = conn1.cursor()
    c.execute("SELECT * FROM Movies")
    items = c.fetchall()
    conn1.commit()
    conn1.close()
    return render_template("hello.html",items=items)

@app.route("/home", methods=["POST" , "GET"])
def home():
    if request.method == 'POST':
        # getting input with name = name in HTML form
        name1 = request.form.get("name")

        # getting input with actor = actor in HTML form
        actor1 = request.form.get("actor")


        # getting input with actor = actor in HTML form
        actress1 = request.form.get("actress")

        director1 = request.form.get("director")

        year1 = request.form.get("year")


        conn1 = sqlite3.connect('movie.db')
        c = conn1.cursor()

        c.execute(" INSERT INTO Movies(name,actor,actress,director,year) VALUES(?,?,?,?,?);",(name1,actor1,actress1,director1,year1))

        c.execute("SELECT * FROM Movies")
        items = c.fetchall()

        conn1.commit()
        conn1.close()
        return render_template("table.html",items=items)
    else:
        conn1 = sqlite3.connect('movie.db')
        c = conn1.cursor()
        c.execute("SELECT * FROM Movies")
        items = c.fetchall()
        conn1.commit()
        conn1.close()
        return render_template("table.html", items=items)

@app.route('/search', methods=["POST" , "GET"])
def search():# put application's code here

    conn1 = sqlite3.connect('movie.db')
    c = conn1.cursor()
    actress1 = request.form.get("actress")
    actor1 = request.form.get("actor")
    #print(name1)
    c.execute("SELECT * FROM movies WHERE actress='{}' or actor='{}'".format(actress1, actor1)  )
    items = c.fetchall()
    #print(items)

    conn1.commit()
    conn1.close()
    return render_template("table.html",items=items)


if __name__ == '__main__':
    app.run()
