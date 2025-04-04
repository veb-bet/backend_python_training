from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Создание базы и модели
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
# Создание соединения с базой данных
engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)
# Создание сессии для работы с базой данных
Session = sessionmaker(bind=engine)
session = Session()
# Добавление нового пользователя
new_user = User(name='Alice', age=25, email='alice@example.com')
session.add(new_user)
session.commit()