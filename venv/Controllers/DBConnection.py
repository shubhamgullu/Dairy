from cassandra.cluster import Cluster


# class DBConnection:
class DBconnection:
    def __init__(self):
        print("Database connection trying......")
        try:
            # con = cql.connect(host="127.0.0.1", port=9042, keyspace="diary")
            cluster = Cluster(['127.0.0.1'])
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

        except ConnectionError:
            print("connection error", ConnectionError)
