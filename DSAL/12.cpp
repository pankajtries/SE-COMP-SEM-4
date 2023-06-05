#include <iostream>
#include <fstream>
using namespace std;

struct Employee {
    int empId;
    char name[50];
    char designation[50];
    double salary;
};

void addEmployee() {
    ofstream file("employees.dat", ios::binary | ios::app);
    if (!file) {
        cout << "Error opening file!" << endl;
        return;
    }

    Employee emp;
    cout << "Enter Employee ID: ";
    cin >> emp.empId;
    cout << "Enter Employee Name: ";
    cin.ignore();
    cin.getline(emp.name, 50);
    cout << "Enter Employee Designation: ";
    cin.getline(emp.designation, 50);
    cout << "Enter Employee Salary: ";
    cin >> emp.salary;

    file.write(reinterpret_cast<char*>(&emp), sizeof(Employee));
    file.close();
}

void deleteEmployee(int empId) {
    fstream file("employees.dat", ios::binary | ios::in | ios::out);
    if (!file) {
        cout << "Error opening file!" << endl;
        return;
    }

    Employee emp;
    bool found = false;
    while (file.read(reinterpret_cast<char*>(&emp), sizeof(Employee))) {
        if (emp.empId == empId) {
            found = true;
            break;
        }
    }

    if (found) {
        emp.empId = -1; // Mark the record as deleted
        long pos = file.tellg();
        file.seekp(pos - sizeof(Employee)); // Move the write position
        file.write(reinterpret_cast<char*>(&emp), sizeof(Employee)); // Overwrite with updated record
        cout << "Employee with ID " << empId << " deleted successfully." << endl;
    } else {
        cout << "Employee with ID " << empId << " not found." << endl;
    }

    file.close();
}

void displayEmployee(int empId) {
    ifstream file("employees.dat", ios::binary);
    if (!file) {
        cout << "Error opening file!" << endl;
        return;
    }

    Employee emp;
    bool found = false;
    while (file.read(reinterpret_cast<char*>(&emp), sizeof(Employee))) {
        if (emp.empId == empId && emp.empId != -1) {
            found = true;
            break;
        }
    }

    if (found) {
        cout << "Employee ID: " << empId << endl;
        cout << "Name: " << emp.name << endl;
        cout << "Designation: " << emp.designation << endl;
        cout << "Salary: " << emp.salary << endl;
    } else {
        cout << "Employee with ID " << empId << " not found." << endl;
    }

    file.close();
}

int main() {
    int choice;
    int empId;

    do {
        cout << "1. Add Employee" << endl;
        cout << "2. Delete Employee" << endl;
        cout << "3. Display Employee" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                addEmployee();
                break;
            case 2:
                cout << "Enter Employee ID to delete: ";
                cin >> empId;
                deleteEmployee(empId);
                break;
            case 3:
                cout << "Enter Employee ID to display: ";
                cin >> empId;
                displayEmployee(empId);
                break;
            case 4:
                cout << "Exiting program." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
                break;
        }
    } while (choice != 4);

    return 0;
}
