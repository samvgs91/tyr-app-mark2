import psycopg2

class BudgetModel:
    def __init__(self, conn):
        self.conn = conn

    def insert_budget(self, name, amount):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO budgets (name, amount) VALUES (%s, %s)",
                (name, amount)
            )
            self.conn.commit()

    def get_all_budgets(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, name, amount FROM budgets ORDER BY id DESC")
            return cur.fetchall()
