import datetime
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
 # generate the list of dic of below
 # [{'Employee': 'Bob', 'YTD Salary': 100000.0}, {'Employee': 'Jan', 'YTD Salary': 150000.0}, {'Employee': 'Erik', 'YTD Salary': 30.0}]
  def calculate_YTD_salary(self, salary):
    current_month = datetime.date.today().month
    ytd_salary = (salary/12) * current_month
    ytd_salary = round(ytd_salary, 2)
    return ytd_salary



class HTMLReportDecorator:
  def __init__(self, report):
    self.html_report = []
    self.report = report
    self.report_methods = [f for f in dir(SalaryYTDReport) if not f.startswith('_')]
    self.report_attributes = [a for a in report.__dict__.keys()]
  
  def __getattr__(self, func):
    if func in self.report_methods:
      def method(*args):
        return getattr(self.report, func)(*args)
      return method
    elif func in self.report_attributes:
      return getattr(self.report, func)
    else:
      raise AttributeError
  
  def report_data(self):
    self.html_report = []
    self.prep_data()
    for row in self.data:
      name = f"<b>{row['Employee']}</b>"
      ytd = f"<i>{row['YTD Salary']}</i>"
      html_row = f"{name}: {ytd}<br />"
      self.html_report.append(html_row)   


def main():
    
    emp1 = Employee('Bob', 100000)
    emp2 = Employee('Jan', 150000)
    emp3 = Employee('Erik', 30)
    report = SalaryYTDReport([emp1, emp2, emp3])
    report = HTMLReportDecorator(report)
    report.prep_data()
    report.report_data()  # create teh report
    report.html_report    # show the report
    
    
    # for employee in report.employees:
    #   print(employee.name)

    print("Hello World!")

if __name__ == "__main__":
    main()