#!/bin/python3
"""
Database handler for any queries to manage or fetch data from the db
"""

import sqlite3
import bcrypt

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

            result = dict((self._c.description[i][0], value) \
                for i, value in enumerate(self._c.fetchone()))

            return result


    def fetchand(self, table, key1, value1, key2, value2):

        with self._conn:

            self._c.execute("""
                SELECT * FROM {table} WHERE
                {column1} LIKE :value1
                and
                {column2} IS :value2
                """.format(table=table, column1=key1, column2=key2),
                            {
                                "value1": value1,
                                "value2": value2
                            })

            result = dict((self._c.description[i][0], value) \
                for i, value in enumerate(self._c.fetchone()))

            return result


    def fetchall(self, table):

        with self._conn:

            self._c.execute("SELECT * FROM {table}".format(table=table))

            result = [dict((self._c.description[i][0], value) \
                for i, value in enumerate(row)) for row in self._c.fetchall()]

            return result


    def fetchall_match_column(self, table, column, match):

        with self._conn:

            self._c.execute("""
                SELECT * FROM {table}
                WHERE {column} IS :match
                """.format(table=table, column=column), {'match': match})

            result = [dict((self._c.description[i][0], value) \
                for i, value in enumerate(row)) for row in self._c.fetchall()]

            return result


    def fetch_users(self):

        with self._conn:

            self._c.execute("SELECT user FROM users")

            users = [dict((self._c.description[i][0], value) \
                for i, value in enumerate(row)) for row in self._c.fetchall()]

            def append_travels(user):

                travels = self.fetch_travels(user['user'])

                user['travels'] = travels

                return user

            result = list(map(append_travels, users))

            return result


    def fetch_user(self, name):

        with self._conn:

            self._c.execute("SELECT user FROM users WHERE user = :name",
                            {'name': name})

            user = dict((self._c.description[i][0], value) \
                for i, value in enumerate(self._c.fetchone()))

            travels = self.fetch_travels(user['user'])

            user['wish-list'] = travels

            return user


    def fetch_user_account(self, name):

        with self._conn:

            self._c.execute("SELECT * FROM users WHERE user = :name",
                            {'name': name})

            user = dict((self._c.description[i][0], value) \
                for i, value in enumerate(self._c.fetchone()))

            return user


    def fetch_travels(self, username):

        with self._conn:

            self._c.execute("SELECT * FROM travel WHERE user = :name",
                            {'name': username})

            result = [dict((self._c.description[i][0], value) \
                for i, value in enumerate(row)) for row in self._c.fetchall()]

            return result


    def fetch_votes(self, username, country, city):

        with self._conn:

            self._c.execute("""
                SELECT votes FROM travel
                WHERE user IS :user
                AND country LIKE :country
                AND city LIKE :city""",
                            {
                                'user': username,
                                'country': country,
                                'city': city
                            })

            result = int(self._c.fetchone()[0])

            return result


    def insert_vote(self, username, country, city, votes):

        with self._conn:

            self._c.execute("""
                UPDATE travel
                SET votes = :votes
                WHERE user IS :user
                AND country LIKE :country
                AND city LIKE :city""",
                            {
                                'votes': votes,
                                'user': username,
                                'country': country,
                                'city': city
                            })


    def insert_user(self, username, password):

        with self._conn:

            password_encrypt = bcrypt.hashpw(
                password.encode('utf-8'), bcrypt.gensalt())

            self._c.execute("""
                INSERT INTO users VALUES
                (:username, :password)
                """, {
                    'username': username,
                    'password': password_encrypt
                    })


    def insert_travel(self, user, country, city):

        with self._conn:

            self._c.execute("""
                INSERT INTO travel VALUES
                (:user, :country, :city, 0)
                """, {
                    'user': user,
                    'country': country,
                    'city': city
                    })


    def delete_travel(self, user, country, city):

        with self._conn:

            self._c.execute("""
                DELETE FROM travel
                WHERE user IS :user
                AND country LIKE :country
                AND city LIKE :city
                """, {
                    'user': user,
                    'country': country,
                    'city': city
                    })
