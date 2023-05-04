import pytest
import pyodbc as odbc


@pytest.fixture(scope='module')
def adv_connection():
    conn = odbc.connect(
        'Driver={SQL SERVER};'
        'Server=EPINCHEW00FB;'
        'Database=AdventureWorks2012;'
        'Trusted_Connection=yes;'
    )
    yield conn
    conn.close()


@pytest.fixture()
def adv_cursor(adv_connection):
    cursor = adv_connection.cursor()
    yield cursor
    adv_connection.rollback()


@pytest.fixture(scope='module')
def trn_connection():
    conn = odbc.connect(
        'Driver={SQL SERVER};'
        'Server=EPINCHEW00FB;'
        'Database=TRN;'
        'Trusted_Connection=yes;'
    )
    yield conn
    conn.close()


@pytest.fixture()
def trn_cursor(trn_connection):
    cursor = trn_connection.cursor()
    yield cursor
    trn_connection.rollback()
