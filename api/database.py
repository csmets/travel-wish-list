#!/bin/python3
"""
Database handler for any queries to manage or fetch data from the db
"""

import sqlite3

class Database:

    def __init__(self):

        self._conn = sqlite3.connect('travel-wish-list.db')

        self._c = self._conn.cursor()


    def fetch(self, table, key, value):

        with self._conn:

            self._c.execute(
                "SELECT * FROM {table} WHERE {column} LIKE :value"
                .format(table=table, column=key),
                {
                    'value': value
                }
            )

            result = [dict((self._c.description[i][0], value) \
                for i, value in enumerate(self._c.fetchone()))]

            return result


    def fetchAnd(self, table, key1, value1, key2, value2):

        with self._conn:

            self._c.execute("""
                SELECT * FROM {table} WHERE
                {column1} LIKE :value1
                AND
                {column2} IS :value2
                """.format(table=table, column1=key1, column2=key2),
                            {
                                "value1": value1,
                                "value2": value2
                            })

            result = [dict((self._c.description[i][0], value) \
                for i, value in enumerate(self._c.fetchone()))]

            return result
