from cs50 import *
from flask import *
app = Flask(__name__)
per=None
db=SQL("sqlite:///match50.db")
@app.route("/")
def index():
  return render_template("homepage.html")
@app.route("/login")
def login():
  return render_template("login.html")
@app.route("/register")
def register():
  return render_template("register.html")
@app.route("/registered",methods=["POST"])
def registered():
  count=0;
  rname=request.form.get("rname")
  rpassword=request.form.get("rpassword")
  cpassword=request.form.get("cpassword")
  email=request.form.get("email")
  date=request.form.get("date")
  month=request.form.get("month")
  year=request.form.get("year")
  gender=request.form.get("gender")
  if(rpassword!=cpassword):
    return render_template("passworderror.html")
  if not "com" in email:
    return render_template("iderror.html")
  if (not rname or not email or not rpassword or not cpassword or not email or not month or not year or not gender) or (rpassword!=cpassword) or ( not ".com" in email):
    return render_template("failure.html")
  repname=db.execute("SELECT* FROM registrants WHERE rname = %s",rname)
  for name in repname:
    count=count+1
  if count>=1 :
    return render_template("already.html")
  db.execute("CREATE TABLE IF NOT EXISTS 'registrants' ( 'rname' TEXT, 'rpassword' TEXT, 'email' TEXT,'date' INT,'month' TEXT,'year' INT,'interest' TEXT);")
  db.execute("INSERT INTO registrants(rname,rpassword,email,date,month,year) VALUES (%s, %s, %s,%s,%s,%s)",rname,rpassword,email,date,month,year)
  return "You are registered!"
lame=None
@app.route("/use",methods=["POST"])
def user():
  global lame
  lame=request.form.get("lname")
  lpassword=request.form.get("lpassword")
  repname=db.execute("SELECT* FROM registrants WHERE rname = %s AND rpassword=%s",lame,lpassword)
  count=0;
  for name in repname:
    count=count+1
  if count!=1 :
    return render_template("fault.html")
  return render_template("user.html",name=lame)
l1=lame
@app.route("/test",methods=["POST","GET"])
def test():
  q=db.execute("SELECT q1 FROM registrants WHERE rname=%s",lame)
  k=q[0]['q1']
  if(k==1 or k==-1):
    return render_template("retest.html")
  else:
    return render_template("test.html")
@app.route("/retest",methods=["POST","GET"])
def retest():
  return render_template("test.html")
@app.route("/hpage",methods=["POST" ,"GET"])
def hpage():
  return render_template("user.html")
@app.route("/submit",methods=["post","GET"])
def submit():
  q1=request.form.get("q1")
  q2=request.form.get('q2')
  q3=request.form.get("q3")
  q4=request.form.get("q4")
  q5=request.form.get("q5")
  q6=request.form.get("q6")
  q7=request.form.get("q7")
  q8=request.form.get("q8")
  q9=request.form.get("q9")
  q10=request.form.get("q10")
  q11=request.form.get("q11")
  q12=request.form.get("q12")
  q13=request.form.get("q13")
  q14=request.form.get("q14")
  q15=request.form.get("q15")
  q16=request.form.get("q16")
  q17=request.form.get("q17")
  q18=request.form.get("q18")
  q19=request.form.get("q19")
  q20=request.form.get("q20")
  db.execute("UPDATE registrants SET q1=%s WHERE rname=%s",q1,lame)
  db.execute("UPDATE registrants SET q2=%s WHERE rname=%s",q2,lame)
  db.execute("UPDATE registrants SET q3=%s WHERE rname=%s",q3,lame)
  db.execute("UPDATE registrants SET q4=%s WHERE rname=%s",q4,lame)
  db.execute("UPDATE registrants SET q5=%s WHERE rname=%s",q5,lame)
  db.execute("UPDATE registrants SET q6=%s WHERE rname=%s",q6,lame)
  db.execute("UPDATE registrants SET q7=%s WHERE rname=%s",q7,lame)
  db.execute("UPDATE registrants SET q8=%s WHERE rname=%s",q8,lame)
  db.execute("UPDATE registrants SET q9=%s WHERE rname=%s",q9,lame)
  db.execute("UPDATE registrants SET q10=%s WHERE rname=%s",q10,lame)
  db.execute("UPDATE registrants SET q11=%s WHERE rname=%s",q11,lame)
  db.execute("UPDATE registrants SET q12=%s WHERE rname=%s",q12,lame)
  db.execute("UPDATE registrants SET q13=%s WHERE rname=%s",q13,lame)
  db.execute("UPDATE registrants SET q14=%s WHERE rname=%s",q14,lame)
  db.execute("UPDATE registrants SET q15=%s WHERE rname=%s",q15,lame)
  db.execute("UPDATE registrants SET q16=%s WHERE rname=%s",q16,lame)
  db.execute("UPDATE registrants SET q17=%s WHERE rname=%s",q17,lame)
  db.execute("UPDATE registrants SET q18=%s WHERE rname=%s",q18,lame)
  db.execute("UPDATE registrants SET q19=%s WHERE rname=%s",q19,lame)
  db.execute("UPDATE registrants SET q20=%s WHERE rname=%s",q20,lame)
  if not q1  or not q2 or not q3 or not q4 or not q5 or not q6 or not q7 or not q8 or not q9 or not q10 or not q11 or not q12 or not q13 or not q14 or not q15 or not q16 or not q17 or not q18 or not q19 or not q20:
    return render_template("failure.html")
  if int(q1)+int(q2)+int(q3)+int(q4)+int(q5)>3:
    p1="E"
  else:
    p1="I"
  if int(q6)+int(q7)+int(q8)+int(q9)+int(q10)>3:
    p2="S"
  else:
    p2="N"
  if int(q11)+int(q12)+int(q13)+int(q14)+int(q15)>3:
    p3="T"
  else:
    p3="F"
  if int(q16)+int(q17)+int(q18)+int(q19)+int(q20)>3:
    p4="J"
  else:
    p4="P"
  db.execute("UPDATE registrants SET p1=%s WHERE rname=%s",p1,lame)
  db.execute("UPDATE registrants SET p2=%s WHERE rname=%s",p2,lame)
  db.execute("UPDATE registrants SET p3=%s WHERE rname=%s",p3,lame)
  db.execute("UPDATE registrants SET p4=%s WHERE rname=%s",p4,lame)
  global per
  per=p1+p2+p3+p4
  db.execute("UPDATE registrants SET perd=%s WHERE rname=%s",per,lame)
  return render_template("user.html",name=lame)
@app.route("/match",methods=["POST","GET"])
def match():
  per=db.execute("SELECT perd FROM registrants WHERE rname=%s",lame)
  o=per[0]['perd']
  p1=db.execute("SELECT email FROM registrants WHERE perd=%s EXCEPT SELECT email FROM registrants WHERE perd=%s AND rname=%s",o,o,lame)
  p2=db.execute("SELECT p2 FROM registrants WHERE rname=%s",lame)
  p3=db.execute("SELECT p3 FROM registrants WHERE rname=%s",lame)
  p4=db.execute("SELECT p4 FROM registrants WHERE rname=%s",lame)
  return f"{o} {p1}"



