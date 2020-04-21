from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///db.sqlite3') # mine is set to 'sqlite:///db.sqlite3'
db = scoped_session(sessionmaker(bind=engine))

def main():
    # create tables
    db.execute("CREATE TABLE courses (cid INTEGER PRIMARY KEY, cname VARCHAR(200) NOT NULL, curl VARCHAR(200) NOT NULL)")
    db.execute("CREATE TABLE tasks (tid INTEGER PRIMARY KEY, tname VARCHAR(200) NOT NULL, turl VARCHAR(200) NOT NULL, type VARCHAR(50) NOT NULL, cid_fk INTEGER NOT NULL, FOREIGN KEY (cid_fk) REFERENCES courses (cid))")
    print("2 tables created")

    print("Committing...")
    db.commit()
    print("Done.")

if __name__ == '__main__':
    main()
