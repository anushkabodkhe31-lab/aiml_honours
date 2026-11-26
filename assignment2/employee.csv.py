"""
Employee Management System (CSV CRUD)

A menu-driven program to add, view, search, update and delete
employees. All data is stored in a CSV file called employee.csv.
"""

import csv
import os


class Employee:
    def __init__(self, filename="employee.csv"):
        self.filename = filename
        self.create_file_if_missing()

    def create_file_if_missing(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["id", "name", "dept", "salary"])

    def read_all_rows(self):
        """Return every row in the file (including the header) as a list."""
        with open(self.filename, "r", newline="") as file:
            return list(csv.reader(file))

    def write_all_rows(self, rows):
        """Replace the whole file with the given list of rows."""
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    def id_exists(self, emp_id):
        for row in self.read_all_rows()[1:]:
            if row[0] == emp_id:
                return True
        return False

    def add_employee(self):
        emp_id = input("Enter employee ID: ").strip()

        if self.id_exists(emp_id):
            print("An employee with this ID already exists.")
            return

        name = input("Enter name: ").strip()
        dept = input("Enter department: ").strip()
        salary = input("Enter salary: ").strip()

        # "a" adds the new row at the end without touching old data
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([emp_id, name, dept, salary])

        print("Employee added successfully.")

    def view_all(self):
        rows = self.read_all_rows()

        if len(rows) == 1:
            print("No employees found.")
            return

        print(f"\n{'ID':<8}{'Name':<20}{'Dept':<15}{'Salary':<10}")
        print("-" * 53)
        for row in rows[1:]:
            print(f"{row[0]:<8}{row[1]:<20}{row[2]:<15}{row[3]:<10}")

    def search_employee(self):
        emp_id = input("Enter employee ID to search: ").strip()

        for row in self.read_all_rows()[1:]:
            if row[0] == emp_id:
                print(f"\nID: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"Department: {row[2]}")
                print(f"Salary: {row[3]}")
                return

        print("Employee not found.")

    def update_employee(self):
        emp_id = input("Enter employee ID to update: ").strip()
        rows = self.read_all_rows()
        found = False

        for row in rows[1:]:
            if row[0] == emp_id:
                found = True
                print("Press Enter to keep the current value.")

                new_name = input(f"Name [{row[1]}]: ").strip()
                new_dept = input(f"Department [{row[2]}]: ").strip()
                new_salary = input(f"Salary [{row[3]}]: ").strip()

                # Only change a field if the user typed something
                if new_name:
                    row[1] = new_name
                if new_dept:
                    row[2] = new_dept
                if new_salary:
                    row[3] = new_salary
                break

        if found:
            self.write_all_rows(rows)
            print("Employee updated successfully.")
        else:
            print("Employee not found.")

    def delete_employee(self):
        emp_id = input("Enter employee ID to delete: ").strip()
        rows = self.read_all_rows()

        # Keep the header, and keep every row except the one being deleted
        remaining = [rows[0]] + [row for row in rows[1:] if row[0] != emp_id]

        if len(remaining) == len(rows):
            print("Employee not found.")
        else:
            self.write_all_rows(remaining)
            print("Employee deleted successfully.")

def main():
    emp = Employee()

    while True:
        print("\n===== Employee Management System =====")
        print("1. Add a new employee")
        print("2. View all employees")
        print("3. Search an employee by ID")
        print("4. Update an employee")
        print("5. Delete an employee")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            emp.add_employee()
        elif choice == "2":
            emp.view_all()
        elif choice == "3":
            emp.search_employee()
        elif choice == "4":
            emp.update_employee()
        elif choice == "5":
            emp.delete_employee()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()