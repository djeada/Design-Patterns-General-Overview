"""
In this example, the Database class implements the Singleton pattern by ensuring that only one instance of the class can be created. This is done by making the constructor private and providing a static method called get_instance() to create or retrieve the instance.

When get_instance() is called, it checks whether an instance of the Database class has already been created. If so, it returns that instance. Otherwise, it creates a new instance of the class and returns it.

The example demonstrates that calling get_instance() multiple times returns the same instance of the Database class. This ensures that all clients of the Database class use the same database connection.

Additionally, the query() method is provided to execute SQL queries on the database. This method can be called on the singleton instance of the Database class, which ensures that all queries are executed on the same database connection.
"""


class Database:
    __instance = None

    @staticmethod
    def get_instance():
        if Database.__instance is None:
            Database()
        return Database.__instance

    def __init__(self):
        if Database.__instance is not None:
            raise Exception("Only one instance of Database is allowed.")
        else:
            Database.__instance = self

    def query(self, sql):
        print(f"Executing query: {sql}")


# Usage example
db1 = Database.get_instance()
db2 = Database.get_instance()
print(db1 is db2)  # Output: True

db1.query("SELECT * FROM users")
db2.query("SELECT * FROM orders")
