from src.general_example import GeneralExample

GE =GeneralExample

def test_flatten_dictionary():
    text = {'key1': [3, 2, 1], 'key2': [42, 55, 10], 'key3': [0, 22]}
    expected = [0, 1, 2, 3, 10, 22, 42, 55]

    actual = GE.flatten_dictionary(text)

    assert expected == actual

def test_load_employee_rec_from_database():
    expected = ['emp001', 'Sam', '100000']

    actual = GE().load_employee_rec_from_database()

    assert expected == actual

def test_fetch_emp_details():
    
    expected = {
            'empId':'emp001',
            'empName': 'Sam',
            'empSalary':'100000'
        }

    actual = GE().fetch_emp_details()

    assert expected == actual