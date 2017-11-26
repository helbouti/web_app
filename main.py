import sys
import logging
import glob
import data_model
from data_model import *
from datetime import datetime as dt
#str(dt.now())

#import webview as wv

from flask import Flask,render_template,request

data_model.dbconnect()
data_model.create_database()

try:
    file=open("10_2017.csv");
except IOError:
    print("10_2017.csv:FILE NOT FOUND!")
    sys.exit(3)



app=Flask(__name__)

@app.route("/import_to_db/<csv_file_name>")
def import_to_db(csv_file_name):
    csv_file=open(csv_file_name)
    fellahs=[]
    mois=Mois.get_or_create(label=csv_file_name.split(".")[0], designation="Imported From File "+csv_file_name)
    for line in csv_file:
        fellah_full_name=line.split(",")[0]
        try:
            total=int(line.split(",")[32])
        except:
            print(csv_file_name+":"+fellah_full_name+"total exception ; total is set to 0")
            total=0

        f=Fellah.get_or_create(full_name=fellah_full_name)


        l=Lait.get_or_create(
            idfellah=f[0].id
            ,idmois=mois[0].id
            ,totale=total
            ,prixu=3800
        )

        #print(csv_file_name+":"+str(f[0].id)+":"+f[0].full_name+":"+str(l[0].totale))
        fellahs.append(f)

    csv_file.close()
    for item in Lait.select():
        print(item.totale)
    return render_template("import_to_db.html",fellahs=fellahs)




@app.route("/uploader", methods=['POST', 'GET'])
def uploader():
    if request.method=="POST":
        f= request.files["csv_file"]
        f.save(f.filename)
        return render_template("upload.html")


names=[]
count=0
for count,line in enumerate(file,1):
    names.append( (count,line.split(",")[0]) )


@app.route("/list")
def list():
        return render_template("list.html",names=names)



@app.route("/find", methods=['POST', 'GET'])
def find():
    find_names = []
    count=0
    file.seek(0)
    if request.method == "POST":
        for count,line in enumerate(file,1):
            tofind=str(request.form["username"]).upper()
            if  tofind in line.split(",")[0].upper():
                print(line.split(",")[0])
                #we are using tuple here
                find_names.append((count,line.split(",")[0]))

        return render_template("list.html", names=find_names)

    else:
        return render_template("list.html", names=names)



def readline(id):
    for count, line in enumerate(file, 1):
        if count==id:
            return line.split(",")


@app.route("/profile/<int:id>")
def profile(id):
    global file
    file.seek(0)
    return render_template("profile.html",values=readline(id))


@app.route("/")
def about():
    return  render_template("home.html")


@app.route("/upload")
def home():
    folder=glob.glob("*.csv")
    print(folder)
    return  render_template("upload.html",folder=folder)


@app.route("/select_cvs/<csv_file>")
def select_cvs(csv_file):
    try:
        global file
        global names
        file = open(csv_file);
        names = []
        count = 0
        for count, line in enumerate(file, 1):
            names.append((count, line.split(",")[0]))

        return render_template("list.html",names=names)
    except IOError:
        print(csv_file+":FILE NOT FOUND!")
    return  csv_file+":FILE NOT FOUND!"



#wv.create_window("myapp","http://0.0.0.0:5000")
#app.run(debug=True,host="0.0.0.0")

