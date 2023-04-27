# Test cases on TRN database
# Employee hire date should not be greater than current date
import pytest
def test_hire_date(trn_cursor):
    trn_cursor.execute("select hire_date from hr.employees where hire_date > GETDATE()")
    hire_date = trn_cursor.fetchall()
    assert len(hire_date) == 0, "Employee hire date is greater than the current date"


# Employee minimum and maximum salary validation
def test_min_max_sal(trn_cursor):
    trn_cursor.execute("select min(salary), max(salary) from hr.employees")
    min_max_sal = trn_cursor.fetchall()
    assert list(min_max_sal[0]) == [2500.00, 24000.00], "Employee salary is not in range"
