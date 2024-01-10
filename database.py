from sqlalchemy import create_engine, text

string_conexao = (
    "mysql+pymysql://tq19uykrk9a9jfwjv58o:pscale_pw_JiIzsNw7TC6PDnThgniXzVLmYm3WLIzbRaqKJ4lJldR@aws.connect.psdb.cloud/carreiras-python?charset=utf8mb4"
)
engine = create_engine(string_conexao,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM vagas"))
  print(result.all())
