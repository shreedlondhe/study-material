import pytest


@pytest.mark.parametrize("username,password",
                         [
                             ("user", "pass"),
                             ("Karan", "Devendra@123"),
                             ("Devendra", "Karan@123"),
                             ("Vijay", "Vijay@987")
                         ]
                         )
def test_login(username, password):
    print(username + ' ' + password)
    # get username
    # get password
    # compare username and password
    # test case pass/fail