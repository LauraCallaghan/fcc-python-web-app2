import sqlalchemy
from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://pb2ggzp18d15r6beopu4:pscale_pw_6T7rI3DH5b03qXJH0Qvm5H5KJGg1gvVLOSFf2yJx1gS@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={"ssl": {
        "ssl_ca": "/etc/ssl/ca-bundle.pem"
    }})

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_dicts = []
    for row in result.all():
      result_dicts.append(row._mapping)
    print(result_dicts)
  

