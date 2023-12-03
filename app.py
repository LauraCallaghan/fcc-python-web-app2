from flask import Flask, render_template, jsonify
from database import engine, load_jobs_from_db

app = Flask(__name__)


@app.route("/")
def hello_jovian():
  jobslist = load_jobs_from_db()
  return render_template('home.html', jobs=jobslist, company_name='Jovian')


@app.route("/api/jobslist")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
