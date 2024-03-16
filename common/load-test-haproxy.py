import random
import time

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError, PendingRollbackError


mysql_url = "mysql+pymysql://root:secret@192.168.160.5/stage"


def insert_into_user(db, u):
    stmt =  ('INSERT INTO users ('
            'username) VALUES')
    stmt = f"{stmt} ('{u}');"
    q = db.execute(text(stmt))
    db.commit()

def select_by_id(db, id):
    stmt = f"SELECT * FROM users WHERE id={id};"
    q = db.execute(text(stmt))
    return q.fetchone()


def main():
    engine = create_engine(mysql_url, pool_pre_ping=True)
    sess = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    with sess() as db:
        q = db.execute(text('SELECT max(id) FROM users;'))
        max_id = q.fetchone()[0]
        st = time.time()
        cnt = 0
        for i in range(100000):
            id = random.randrange(1, max_id)
            try:
                select_by_id(db, id)
            except OperationalError:
                pass
            except PendingRollbackError:
                db.rollback()
                print('exception PendingRollbackError')
                time.sleep(0.05)
                pass
            end = time.time()
            cnt += 1
            if (end - st) > 1:
                print(cnt)
                st = time.time()
                cnt = 0

main()
