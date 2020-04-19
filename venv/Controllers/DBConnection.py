
from cassandra.cluster import Cluster



class DatabaseConnection:
    def __init__(self):
        print("trying connection establishment......")


    def Connection(self):
        print("check database connection .......")
        try:
            # con = cql.connect(host="127.0.0.1", port=9042, keyspace="diary")
            cluster = Cluster([ '127.0.0.1' ])
            session = cluster.connect('diary')
            print("connection Successfully ")
            session.execute('USE diary')
            rows = session.execute("SELECT * FROM emp;")

            for row in rows:
                print(row.emp_city)
                print(row.emp_name)
                print(row.emp_phone)
                print(row.emp_sal)

                print(row.emp_id)

            final = """INSERT INTO emp (emp_id, emp_name, emp_city, emp_phone, emp_sal)
           VALUES(5,'rahman', 'Chennai', 9848022330, 45000);"""

            schema = 'emp_id,emp_city,emp_name,emp_phone,emp_sal'

            session.execute(final)

        except ConnectionError:
            print("connection error", ConnectionError)