import sqlalchemy
from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
    db_connection_string,
    connect_args={"ssl": {
        "ssl_ca": "/etc/ssl/ca-bundle.pem"
    }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    rows = result.all()
    jobs = []
    for row in rows:
      jobs.append(dict(row._mapping))
      #print(type(jobs))
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :val"),
    {'val': id})
    job = []
    rows = result.all()
    for row in rows:
      job.append(dict(row._mapping))
    if len(job) == 0:
      return None
    else:
      return job[0]

def add_application_to_db(job_id,data):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO applications (job_id, full_name, email, linkedin, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin, :education, :work_experience, :resume_url)")
   
    conn.execute(query, job_id=job_id,full_name=data['full_name'], email=data['email'], linkedin=data['linkedin'], education=data['education'], work_experience=data['work_experience'], resume_url=data['resume_url'])
