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
                       , ("A3", "0", "12"),
                       ("B1", "1", "100"),
                        ("B2", "0", "80")
                       , ("B3", "0", "12") ;
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




def create_table_bank():
    connection=sqlite3.connect("banking.db")
    connection.execute("""
    CREATE TABLE "cards" (
	"type"	TEXT,
	"number"	INTEGER,
    "cvc" INTEGER, 
    "holder" TEXT, 
	"balance"	REAL
    );
    """)
    connection.commit()
    connection.close()


def insert_data_bank():
    connection=sqlite3.connect("banking.db")
    connection.execute(""" 
    INSERT INTO "cards" VALUES
                        ("master card", "23456789","234", "marry smith", "2000"),
                        ("visa", "12345678","123", "john smith", "450")
                        ;
    """)
    connection.commit()
    connection.close()

def select_all_bank():
    connection=sqlite3.connect("banking.db")
    #for read operations we need a cursor obj:
    cursor= connection.cursor()
    cursor.execute("""
                    SELECT * from "cards"
                   """)
    result=cursor.fetchall()
    connection.close()
    return result



# create_table()
# insert_data()
# create_table_bank()
insert_data_bank()