from sqlalchemy import create_engine, text

string_conexao = "mysql+pymysql://dk1237r0wncsx31wpejq:pscale_pw_1XDJi9TCPQxf0tg6bSjM4hPFQUoH0GRf0EIDfuZFJjw@aws.connect.psdb.cloud/carreiras-python?charset=utf8mb4"
engine = create_engine(string_conexao,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

def carrega_vagas_db():
      with engine.connect() as conn:
        resultado = conn.execute(text("SELECT * FROM vagas"))
        vagas = []
        for vaga in resultado.all():
          vagas.append(vaga._asdict())
        return vagas
