from sqlalchemy import create_engine, text

string_conexao = "mysql+pymysql://xqftj4cfhldtamtybhj5:pscale_pw_z9YICD2BRR5t5gbbyvRHgPkp949uvSrT6Waiyu2nlPb@aws.connect.psdb.cloud/carreiras-python?charset=utf8mb4"
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
