#import hr
import employees

salary_employee = employees.SalaryEmployee(1, 'Amit Singh', 10000)
hourly_employee =  employees.HourlyEmployee(2, 'Aps', 40, 42)
commission_employee = employees.CommissionEmployee(3, 'Sweety', 4000, 350)
payroll_system = employees.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])
