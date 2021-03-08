import hr

salary_employee = hr.SalaryEmployee(1, 'Amit Singh', 10000)
hourly_employee =  hr.HourlyEmployee(2, 'Aps', 40, 42)
commission_employee = hr.CommissionEmployee(3, 'Sweety', 4000, 350)
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])
