import re
from flask import Flask,request,render_template
import json

class Employee:
    def __init__(self,Eid,Ename,Esal,HRA,DA,Ded):
        self.Eid = Eid
        self.Ename = Ename
        self.Esal = Esal
        self.HRA = HRA
        self.DA = DA
        self.Ded = Ded
    def __eq__(self,other):
        if(isinstance(other,type(self))):
            eq = True
            eq = eq and (self.Eid == other.Eid)
            eq = eq and (self.Ename == other.Ename)
            eq = eq and (self.Esal == other.Esal)
            eq = eq and (self.HRA == other.HRA)
            eq = eq and (self.DA == other.DA)
            eq = eq and (self.Ded == other.Ded)
            return(eq)

volatile_db = []

app = Flask(__name__,static_url_path='', static_folder='',template_folder='')

@app.route("/")
def mainPage():
    return render_template('index.html')

@app.route("/api/EmpData",methods=['get'])
def getData():
    try:
        Eid = request.args.get('Eid')
    except:
        data = {'Eid' : None}
        return(json.dumps(data))
    for i in volatile_db:
        if(i.Eid == Eid):
            data = {
                'Eid' : i.Eid,
                'Ename': i.Ename,
                'Esal' : i.Esal,
                'HRA' : i.HRA,
                'DA' : i.DA,
                'Ded' : i.Ded
            }
            return(json.dumps(data))
    data = {'Eid' : None}
    return(json.dumps(data))

@app.route("/api/AddData",methods=['get'])
def AddData():
    try:
        print(request.args)
        Eid = request.args.get('Eid')
        Ename = request.args.get('Ename')
        Esal = request.args.get('Esal')
        HRA = request.args.get('Ehra')
        DA = request.args.get('Eda')
        Ded = request.args.get('Eded')   
        volatile_db.append(Employee(Eid,Ename,Esal,HRA,DA,Ded))
        return(render_template('result.html',state='Sucess!'))
    except:
        return(render_template('result.html',state='Failed!'))

@app.route("/api/ChangeData",methods=['get'])
def ChangeData():
    try:
        Eid = request.args.get('Eid')
        Ename = request.args.get('Ename')
        Esal = request.args.get('Esal')
        HRA = request.args.get('Ehra')
        DA = request.args.get('Eda')
        Ded = request.args.get('Eded')   
        for i in range(len(volatile_db)):
            if(volatile_db[i].Eid == Eid):
                volatile_db[i]=Employee(Eid,Ename,Esal,HRA,DA,Ded)
        print(volatile_db)
        return(render_template('result.html',state='Sucess!'))
    except Exception as ex:
        return(str(ex))


app.run(debug=True)