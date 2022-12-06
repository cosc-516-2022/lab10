from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import csv


class CassandraDB():

    def connect(self):
        #TODO: connect to database

    def create_table(self):
        # TODO: create a table with proper schema, PLEASE NAME IT "Customer"

    def load_data(self):
        #TODO: load customer.csv into the table created

    def query_1(self):
        # TODO: write query 1 that returns the age of the customer whose id is 979863
        return

    def query_2(self):
        #TODO: write query 2 that returns information of customers who are “MALE” and age is 25 or 35. Return it as a list
        return q2.all()


if __name__ == '__main__':
    client = CassandraDB()
    client.connect()
    client.create_table()
    client.load_data()
    client.query_1()
    client.query_2()