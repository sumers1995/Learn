import sqlite3
from typing import Any
from contextlib import contextmanager
from app.models import ShipmentCreate, ShipmentStatus, ShipmentUpdate

class Database:
    # def __init__(self) -> None:
    #     self.conn = sqlite3.connect("sqlite.db", check_same_thread=False)
    #     self.cur = self.conn.cursor()
    #     self.create_table()

    def connect_to_db(self):
        self.conn = sqlite3.connect("sqlite.db", check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS shipment (
                id INTEGER PRIMARY KEY, 
                content TEXT, 
                weight REAL,
                destination INTEGER, 
                status TEXT
                )""")
        
    def create(self, shipment: ShipmentCreate) -> int:
        self.cur.execute(""" SELECT MAX(id) FROM shipment""")
        id = self.cur.fetchone()[0]
        new_id = 1033 if id is None else id+1
        self.cur.execute("""INSERT INTO shipment
                         VALUES (:id, :content, :weight, :destination, :status) """,
                         {
                             "id": new_id,
                            **shipment.model_dump(),
                            "status": ShipmentStatus.placed
                         })
        self.conn.commit()
        return new_id

    def get(self, id: int) -> dict[str, Any] | None:
        self.cur.execute("""
                SELECT * FROM shipment
                         WHERE ID = ?
                         """, (id,))
        row = self.cur.fetchone()
        return {"id": row[0],
                "content": row[1],
                "weight": row[2],
                "destination": row[3],
                "status": row[4]
                } if row else None

    def get_all(self):
        self.cur.execute("""
                         SELECT * FROM shipment""")
        return self.cur.fetchall()
    
    def update(self, id: int, shipment: ShipmentUpdate) -> dict[str, Any] | None:
        self.cur.execute("""
                         UPDATE shipment SET status = :status
                         WHERE id = :id
                         """, {
                             "id": id,
                             **shipment.model_dump()
                         })
        self.conn.commit()
        return self.get(id=id)
    
    def delete(self, id: int):
        self.cur.execute("""
                         DELETE FROM shipment
                         WHERE id = ?
                         """, (id,))
        self.conn.commit()

    def close(self):
        self.conn.close()

    # def __enter__(self):
    #     self.connect_to_db()
    #     self.create_table()
    #     return self
    
    # def __exit__(self, *args):
    #     self.close()
    
if __name__ == "__main__":
    # with Database() as db:
    #     print(db.get(1038))
    
    @contextmanager
    def managed_db():
        db = Database()
        #setup
        print("entering setup")
        db.connect_to_db()
        db.create_table()
        yield db
        print("exiting context")
        db.close()

    with managed_db() as db:
        print(db.get(1033))


