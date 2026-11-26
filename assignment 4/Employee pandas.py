"""
Employee Management System (Pandas CRUD)

A menu-driven program to add, view, search, update and delete
employees. Data lives in a pandas DataFrame and is saved to
employee_pandas.csv after every change.
"""

import os
import pandas as pd

FILENAME = "employee_pandas.csv"
COLUMNS = ["id", "name", "dept", "salary"]

def create_file_if_missing():
    if not os.path.exists(FILENAME):
        empty_table = pd.DataFrame(columns=COLUMNS)
        empty_table.to_csv(FILENAME, index=False)


def load_data():
    return pd.read_csv(FILENAME)


def save_data(df):
    df.to_csv(FILENAME, index=False)
def add_employee():
    df = load_data()
    eid = int(input("Enter employee ID: "))

    if not df[df["id"] == eid].empty:
        print("An employee with this ID already exists.")
        return

    name = input("Enter name: ").strip()
    dept = input("Enter department: ").strip()
    salary = float(input("Enter salary: "))

    new_row = pd.DataFrame([[eid, name, dept, salary]], columns=COLUMNS)
    df = pd.concat([df, new_row], ignore_index=True)

    save_data(df)
    print("Employee added successfully.")
    
def view_all():
    df = load_data()

    if df.empty:
        print("No employees found.")
    else:
        print()
        print(df.to_string(index=False))

def search_employee():
    df = load_data()
    eid = int(input("Enter employee ID to search: "))

    result = df[df["id"] == eid]

    if result.empty:
        print("Employee not found.")
    else:
        print()
        print(result.to_string(index=False))

def update_employee():
    df = load_data()
    eid = int(input("Enter employee ID to update: "))

    if df[df["id"] == eid].empty:
        print("Employee not found.")
        return

    print("Press Enter to keep the current value.")
    new_name = input("New name: ").strip()
    new_dept = input("New department: ").strip()
    new_salary = input("New salary: ").strip()
    if new_name:
        df.loc[df["id"] == eid, "name"] = new_name
    if new_dept:
        df.loc[df["id"] == eid, "dept"] = new_dept
    if new_salary:
        df.loc[df["id"] == eid, "salary"] = float(new_salary)

    save_data(df)
    print("Employee updated successfully.")

def delete_employee():
    df = load_data()
    eid = int(input("Enter employee ID to delete: "))

    if df[df["id"] == eid].empty:
        print("Employee not found.")
        return
    df = df[df["id"] != eid]

    save_data(df)
    print("Employee deleted successfully.")
def main():
    create_file_if_missing()

    while True:
        print("\n===== Employee Management System =====")
        print("1. Add a new employee")
        print("2. View all employees")
        print("3. Search an employee by ID")
        print("4. Update an employee")
        print("5. Delete an employee")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        try:
            if choice == "1":
                add_employee()
            elif choice == "2":
                view_all()
            elif choice == "3":
                search_employee()
            elif choice == "4":
                update_employee()
            elif choice == "5":
                delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")
        except ValueError:
            print("Please enter a valid number for ID and salary.")


if __name__ == "__main__":
    main()