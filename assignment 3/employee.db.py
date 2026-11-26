"""
Employee Management System (SQLite CRUD)

A menu-driven program to add, view, search, update and delete
employees. All data is stored in an SQLite database file, employee.db.
"""

import sqlite3


class Employee:
    def __init__(self, db_name="employee.db"):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS employee (
                id     INTEGER PRIMARY KEY,
                name   TEXT,
                dept   TEXT,
                salary REAL
            )
            """
        )
        self.conn.commit()

    def find(self, emp_id):
        self.cur.execute("SELECT * FROM employee WHERE id = ?", (emp_id,))
        return self.cur.fetchone()

    def add(self):
        emp_id = int(input("Enter ID: "))

        if self.find(emp_id):
            print("ID already exists")
            return

        name = input("Enter name: ")
        dept = input("Enter department: ")
        salary = float(input("Enter salary: "))

        self.cur.execute(
            "INSERT INTO employee (id, name, dept, salary) VALUES (?, ?, ?, ?)",
            (emp_id, name, dept, salary),
        )
        self.conn.commit()
        print("Employee added")

    def view(self):
        self.cur.execute("SELECT * FROM employee")
        rows = self.cur.fetchall()

        if not rows:
            print("No employees yet")
            return

        for row in rows:
            print(row)

    def search(self):
        emp_id = int(input("Enter ID to search: "))
        row = self.find(emp_id)

        if row:
            print(row)
        else:
            print("Not found")

    def update(self):
        emp_id = int(input("Enter ID to update: "))

        if not self.find(emp_id):
            print("Not found")
            return

        name = input("Enter new name: ")
        dept = input("Enter new department: ")
        salary = float(input("Enter new salary: "))

        self.cur.execute(
            "UPDATE employee SET name = ?, dept = ?, salary = ? WHERE id = ?",
            (name, dept, salary, emp_id),
        )
        self.conn.commit()
        print("Employee updated")

    def delete(self):
        emp_id = int(input("Enter ID to delete: "))

        if not self.find(emp_id):
            print("Not found")
            return

        self.cur.execute("DELETE FROM employee WHERE id = ?", (emp_id,))
        self.conn.commit()
        print("Employee deleted")

def main():
    emp = Employee()

    while True:
        print("\n1. Add  2. View  3. Search  4. Update  5. Delete  6. Exit")
        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":
                emp.add()
            elif choice == "2":
                emp.view()
            elif choice == "3":
                emp.search()
            elif choice == "4":
                emp.update()
            elif choice == "5":
                emp.delete()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice")
        except ValueError:
            # Happens when the ID or salary is not a number
            print("Please enter a valid number for ID and salary")


if __name__ == "__main__":
    main()