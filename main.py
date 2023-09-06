from flask import Flask, render_template

app = Flask(__name__)
JOBS=[
  {
    'id': 1,
    'title': "Frontend Engineer",
    'Salary': "$120,000",
    'Location': 'New Delhi India'
  },
   {
     'id': 2,
    'title': "Backend Engineer",
    'Salary': "$120,000",
    'Location': 'Washinton, USA'
  },
 {
   'id': 3,
    'title': "Data Analyst",
    'Salary': "$120,000",
    'Location': 'Abuja, Nigeria'
  }
]

@app.route('/')
def index():
  return render_template('home.html', jobs=JOBS)


app.run(host='0.0.0.0', port=81)