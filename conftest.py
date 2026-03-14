##тут напишу пример фикстуры тут питон файл для них фикстура - это подготовка перед выполнением тестов
import pytest

HOST = "https://petstore3.swagger.io/api/v3"


@pytest.fixture(scope="session")
def init_environment():
    ...