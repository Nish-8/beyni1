from flask import Flask, render_template,jsonify
#jsonify id=s used to programitacillay extract file, it does not require rendering the templet

app = Flask(__name__)

JOBS=[
    {"id":1,
     "title":"Web developer",
     "location":"Mumbai,India",
     "salary":"Rs. 1,50,000"

     },
    {"id":2,
     "title":"Backend Developer",
     "location":"Delhi,India",
     "salary":"Rs. 2,50,000"
     },
    {"id":3,
     "title":" Python Tutor",
     "location":"Pune,India",
     "salary":"Rs. 3,50,000"
     },
    {"id":1,
     "title":"Front-end Developer",
     "location":"Varanasi,India",
     "salary":"Rs. 1,60,000"
     }
]



@app.route("/")
def hello_world():
    return render_template("intro.html",company_name="beyni",jobs=JOBS)

@app.route("/api/jobs") #to distinguish usual html file we use /api/
def jobs_list():
    return jsonify(JOBS)

app.run(debug=True)