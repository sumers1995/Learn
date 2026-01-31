const employees = [
      { id: 1, name: 'John Doe', age: 30, department: 'IT', salary: 50000, specialization: 'Javascript'},
      { id: 2, name: 'Alice Smith', age: 28, department: 'HR', salary: 45000, specialization: 'Python' },
      { id: 3, name: 'Bob Johnson', age: 35, department: 'Finance', salary: 60000, specialization: 'Java' },
      { id: 4, name: 'Sumer Sadawarti', age: 30, department: 'Postal', salary: 46000, specialization: 'HTML' },
      { id: 5, name: 'Prabhakar Gangwar', age: 28, department: 'HR', salary: 44000, specialization: 'CSS' },
      //... More employee records can be added here
    ];

function displayEmployees() {
    const totalEmployees = employees.map(employee => `<p>${employee.id}: ${employee.name} - ${employee.department} - ₹${employee.salary}</p>`).join('');
    document.getElementById('employeesDetails').innerHTML = totalEmployees;
}

function calculateTotalSalaries() {
    const totalSalaries = employees.reduce((acc, employee) => acc + employee.salary, 0);
    alert(`Total Salaries: ₹${totalSalaries}`);
}

function displayHREmployees() {
    const hrEmployees = employees.filter(employee => employee.department === 'HR');
    const hrEmployeesDisplay = hrEmployees.map((employee, index) => `<p>${index+1}: ${employee.name} - ${employee.department} - ₹${employee.salary}</p>`).join('');
    document.getElementById('employeesDetails').innerHTML = hrEmployeesDisplay;
}

function findEmployeeById(employeeId) {
    const foundEmployee = employees.find(employee => employee.id === employeeId);
    if (foundEmployee) {
        document.getElementById('employeesDetails').innerHTML = `<p>${foundEmployee.id}: ${foundEmployee.name} - ${foundEmployee.department} - ₹${foundEmployee.salary}</p>`;
    }
    else {
        document.getElementById('employeesDetails').innerHTML = 'no employee with this ID';
    }
}

function findEmployeeBySpecialization(empSpecialization) {
    const foundEmployee = employees.find(employee => employee.specialization === empSpecialization);
    if (foundEmployee) {
        console.log('Found employee')
        document.getElementById('employeesDetails').innerHTML = `<p>${foundEmployee.id}: ${foundEmployee.name} - ${foundEmployee.department} - ₹${foundEmployee.salary}</p>`;
    }
    else {
        document.getElementById('employeesDetails').innerHTML = 'no such employee found'
    }
}
