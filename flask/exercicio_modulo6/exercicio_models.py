from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey


engine = create_engine('sqlite:///exercicio_modulo6/devs.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Programador(Base):
    __tablename__='programador'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)
    email = Column(String(65))
    
    def __repr__(self):
        a = [self.id, self.nome, self.idade, self.email]
        return f'{self.id}: {self.nome} {self.idade} {self.email}'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Habilidades(Base):
    __tablename__='habilidade'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)

    def __repr__(self):
        return f'{self.id}: {self.nome}'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()
  
class ProgramadorHabilidades(Base):
    __tablename__='programador_habilidade'
    id = Column(Integer, primary_key=True)
    programador_id = Column(Integer, ForeignKey('programador.id'))
    habilidade_id = Column(Integer, ForeignKey('habilidade.id'))

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()

