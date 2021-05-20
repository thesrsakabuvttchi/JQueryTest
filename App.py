from flask import Flask,request,render_template

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

app = Flask(__name__,static_url_path='', static_folder='./')

@app.route("/")
def mainPage():
    index = open('index.html')
    return(index.read())

app.run(debug=True)