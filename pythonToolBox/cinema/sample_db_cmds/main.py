import sqlite3


def create_table():
    connection=sqlite3.connect("cinema.db")
    connection.execute("""
    CREATE TABLE "seats" (
	"seat_id"	TEXT,
	"taken"	INTEGER,
	"price"	REAL
    );
    """)
    connection.commit()
    connection.close()


def insert_data():
    connection=sqlite3.connect("cinema.db")
    connection.execute(""" 
    INSERT INTO "seats" ("seat_id","taken", "price") VALUES
                        ("A1", "1", "100"),
                        ("A2", "0", "80")
                       , ("A3", "0", "12") ;
    """)
    connection.commit()
    connection.close()

def select_all():
    connection=sqlite3.connect("cinema.db")
    #for read operations we need a cursor obj:
    cursor= connection.cursor()
    cursor.execute("""
                    SELECT * from "seats"
                   """)
    result=cursor.fetchall()
    connection.close()
    return result


def select_specific_column():
    connection=sqlite3.connect("cinema.db")
    #for read operations we need a cursor obj:
    cursor= connection.cursor()
    cursor.execute("""
                    SELECT "seat_id", "taken" from "seats"
                   """)
    result=cursor.fetchall()
    connection.close()
    return result


def select_with_condition():
    connection=sqlite3.connect("cinema.db")
    #for read operations we need a cursor obj:
    cursor= connection.cursor()
    cursor.execute("""
                    SELECT * from "seats" WHERE "price"> 70
                   """)
    result=cursor.fetchall()
    connection.close()
    return result


def update_value():
    connection=sqlite3.connect("cinema.db")
    connection.execute("""
        UPDATE "seats" SET "taken"=0 WHERE "seat_id"="A3"
        """ )
    connection.commit()
    connection.close()

def update_value_parametric(seat_id, occupied):
    connection=sqlite3.connect("cinema.db")
    connection.execute("""
        UPDATE "seats" SET "taken"=? WHERE "seat_id"=?
        """ , [occupied, seat_id])
    connection.commit()
    connection.close()


def delete_record():
    connection=sqlite3.connect("cinema.db")
    connection.execute("""
        DELETE FROM "seats" WHERE "seat_id"="A3"
        """ )
    connection.commit()
    connection.close()


# print(select_all())
# print(select_specific_column())
# print(select_with_condition())
update_value_parametric("A2", 1)
print(select_all())