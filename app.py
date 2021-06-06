#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
from flask_mysqldb import MySQL
app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='P@ssw0rd'
app.config['MYSQL_DB']='school'

mysql=MySQL(app)

@app.route('/')
def inndf():
    return render_template('demo.html')
@app.route('/info',methods=['GET','POST'])
def kjjhj():
    if(request.method=="POST"):
        name=request.form["n"]
        email=request.form['e']
        course=request.form['c']
        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO student(name,email,course) VALUES(%s,%s,%s)',(name,email,course))
        mysql.connection.commit()
        cur.close()
        return render_template('demo.html')
if __name__=='__main__':
    app.run()

