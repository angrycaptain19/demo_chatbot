import mysql.connector

# Database Configs
HOSTNAME = ' 0.0.0.0'
USER = 'root'
PWD = 'yourpwd'
DATABASE = 'bookings'


class SQlServer:
    """
    Extracts data from column of a table
    """

    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    def intantiate_db(self):
        mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )
        return mydb

    def get_data(self, filters, table, flag=True):
        mydb = self.intantiate_db()
        mycursor = mydb.cursor()
        if flag:
            where_clause = get_where_clause(filters)
            mycursor.execute("SELECT * FROM {0} {1}".format(table, where_clause))
            myresult = mycursor.fetchall()
            return myresult

        else:
            where_clause_occupied = get_where_clause_occupied(filters)
            mycursor.execute("SELECT * FROM {0} {1}".format(table, where_clause_occupied))
            myresult1 = mycursor.fetchall()
            where_clause_not_sanitized = get_where_clause_not_santized(filters)
            mycursor.execute("SELECT * FROM {0} {1}".format(table, where_clause_not_sanitized))
            myresult2 = mycursor.fetchall()
            return myresult1, myresult2


def get_where_clause_occupied(filters):
    str = ''
    default = "WHERE is_santized='Yes' "
    if filters:
        for i, j in filters:
            str = "AND {0}='{1}'".format(i, j)
    default = default + str
    return default


def get_where_clause_not_santized(filters):
    str = ''
    default = "WHERE status is NULL "
    if filters:
        for i, j in filters:
            str = "AND {0}='{1}'".format(i, j)
    default = default + str
    return default


def get_where_clause(filters):
    str=''
    default = "WHERE status is NULL AND is_santized='Yes'"
    if filters:
        for i,j in filters:
            str = "AND {0}='{1}'".format(i,j)
    default=default+str
    return default

