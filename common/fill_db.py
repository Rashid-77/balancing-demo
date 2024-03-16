import random

from faker import Faker

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


mysql_url = "mysql+pymysql://root:secret@192.168.160.2/stage"


def create_table(db):
    stmt = '''
        CREATE TABLE IF NOT EXISTS `users` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `username` CHAR(50) NOT NULL,
        PRIMARY KEY (id)
        );'''
    q = db.execute(text(f"{stmt};"))
    db.commit()


def insert_into_user(db, u):
    stmt =  ('INSERT INTO users ('
            'username) VALUES')
    
    stmt = f"{stmt} ('{u}');"
    q = db.execute(text(stmt))
    db.commit()


def main():
    engine = create_engine(mysql_url, pool_pre_ping=True)
    sess = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    fake = Faker("en_US")

    with sess() as db:
        create_table(db)
        for i in range(5):
            if random.randint(0, 1):
                name = fake.first_name_male()
            else:
                name = fake.first_name_female()
            insert_into_user(db, name.lower())

        q = db.execute(text('SELECT max(id) FROM users;'))
        res = q.fetchone()
        print(res)

main()
