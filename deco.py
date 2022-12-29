

# import datetime
from datetime import datetime

datetime = datetime.now()

import time

class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary


class SalaryYTDReport:
  def __init__(self, employees):
    self.employees = employees
    self.data = []

  def prep_data(self):
    self.data = []
    for employee in self.employees:
      emp_sal_dict = {'Employee': employee.name, 'YTD Salary': self.calculate_YTD_salary(employee.salary)}
      self.data.append(emp_sal_dict)
      #print(self.data)
 # generate the list of dic of below
 # [{'Employee': 'Bob', 'YTD Salary': 100000.0}, {'Employee': 'Jan', 'YTD Salary': 150000.0}, {'Employee': 'Erik', 'YTD Salary': 30.0}]
  def calculate_YTD_salary(self, salary):
    current_month = datetime.today().month
    ytd_salary = (salary/12) * current_month
    ytd_salary = round(ytd_salary, 2)
    return ytd_salary


### logging

class PerformanceLogReportDecorator:
  def __init__(self, report):
    self.report = report
    self.report_methods = [f for f in dir(SalaryYTDReport) if not f.startswith('_')]
    self.report_attributes = [a for a in report.__dict__.keys()]

  def __getattr__(self, func):
    if func in self.report_methods:
      # ==========wrap the method  
      def method(*args):              # wrapp the build in mentod function
        return self.log(func, *args)  # all method call teh log function
      return method
    elif func in self.report_attributes:
      return getattr(self.report, func)
    else:
      raise AttributeError
  
  def log(self, func, *args):
    start = datetime.now()
    getattr(self.report, func)(*args)
    time.sleep(1) # Putting this here to show logging is actually happening
    end = datetime.now()
   # breakpoint()
    microseconds = (end-start).microseconds
    print(f"{func} ran in {microseconds} microseconds")


def main():
    
    emp1 = Employee('Bob', 100000)
    emp2 = Employee('Jan', 150000)
    emp3 = Employee('Erik', 30)
    report = SalaryYTDReport([emp1, emp2, emp3])
    report = PerformanceLogReportDecorator(report)

    report.prep_data()
   
    report.calculate_YTD_salary(333)

#======================================    
# outputs
#     prep_data ran in 1278 microseconds
# calculate_YTD_salary ran in 20336 microseconds


if __name__ == "__main__":
    main()