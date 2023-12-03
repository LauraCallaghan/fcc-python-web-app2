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
    jobs = []
    rows = result.all()
    for row in rows:
      jobs.append(dict(row._mapping))
    if len(rows) == 0:
      return "Job not found"
    else:
      return jobs[0]
