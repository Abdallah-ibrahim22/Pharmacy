import pyodbc


cursor = ''
connection = ''
def ask():
    global cursor , connection
    server = '.'
    database = 'pharmacy'

    connection_string = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'Trusted_Connection=yes;'
    )

    # Establish a connection
    connection = pyodbc.connect(connection_string)

    # Create a cursor from the connection
    cursor = connection.cursor()
    # Example: Execute a SQL query


def show_clients():
    global cursor , connection
    cursor.execute('SELECT * FROM client')

    # Fetch and print the results
    rows = cursor.fetchall()
    
    return rows


def insert_client(id , client_name , phone , address):
    global cursor , connection

    
    # to add vars on the query 
    insert_str = "execute insertClient ? , ? , ? , ?"

    # this how to execute a query with outer parameters
    try :
        cursor.execute(insert_str , (id , client_name , phone , address))
        connection.commit()
        id = 0 ; client_name = phone = address = ''
    except Exception as e : print(e)


def show_bills():
    global cursor , connection
    cursor.execute('select * from bill')

    # Fetch and print the results
    rows = cursor.fetchall()
    
    return rows


def insert_bill(id ,bill_date ,bill_state ,client_id):
    global cursor , connection

    
    # to add vars on the query 
    insert_str = "execute insertBill \
                ?,?,?,?"

    # this how to execute a query with outer parameters
    try :
        cursor.execute(insert_str , (id ,bill_date ,bill_state ,client_id))
        connection.commit()
    except Exception as e : print(e)


def show_medicine():
    global cursor , connection
    cursor.execute('SELECT * FROM medicine')

    # Fetch and print the results
    rows = cursor.fetchall()
    
    return rows


def insert_medicine(id,name,type, amount ,expdate,sell_price ,buy_price ,store_id ):
    global cursor , connection

    # to add vars on the query 
    insert_str = "execute insertMedicine \
        ? , ? , ? , ? , ? , ? , ? , ?"

    # this how to execute a query with outer parameters
    try :
        cursor.execute(insert_str , (id,name,type, amount ,expdate,sell_price ,buy_price ,store_id ))
        connection.commit()
    except Exception as e : print(e)


def show_store():
    global cursor , connection
    cursor.execute('SELECT * FROM store')

    # Fetch and print the results
    rows = cursor.fetchall()
    
    return rows


def insert_store(id,name,phone_number):
    global cursor , connection

    
    # to add vars on the query 
    insert_str = "execute insertStore ? , ? , ? "

    # this how to execute a query with outer parameters
    try :
        cursor.execute(insert_str , (id,name,phone_number))
        connection.commit()
    except Exception as e : print(e)


def show_medicine_bills():
    global cursor , connection
    cursor.execute('execute getAllBills')

    # Fetch and print the results
    rows = cursor.fetchall()
    
    return rows


def insert_medicine_bill(medicine_id,bill_id,medicine_amount):
    global cursor , connection 
    insert_str = "execute insertMedicineBill ? , ? , ?"
    try :
        cursor.execute(insert_str , (medicine_id,bill_id,medicine_amount))
        connection.commit()
    except Exception as e : print(e)



def show_medicine_bill():
    global cursor , connection
    cursor.execute('SELECT * FROM medicine_bill')

    # Fetch and print the results
    rows = cursor.fetchall()
    
    return rows


def insert_medicine_bill(medicine_id , bill_id , amount):
    global cursor , connection

    
    # to add vars on the query 
    insert_str = "insert into medicine_bill values( ? , ? , ? )"

    # this how to execute a query with outer parameters
    try :
        cursor.execute(insert_str , (medicine_id , bill_id , amount))
        connection.commit()
    except Exception as e : print(e)


