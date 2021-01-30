import pytest

@pytest.fixture
def my_fixture():
    return 42


@pytest.fixture
def one_fixture():
    print ('hello world')
    return 'hello world'

@pytest.fixture
def captured_fixture(capsys):
    print('hello')