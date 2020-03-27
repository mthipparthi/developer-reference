import pytest

from selenium import webdriver


@pytest.fixture()
def chrome_browser():
    return webdriver.Chrome("/Users/mahesh.thipparthi/Downloads/chromedriver")


def pytest_addoption(parser):
    group = parser.getgroup("helloworld")
    group.addoption(
        "--name",
        action="store",
        dest="name",
        default="World",
        help='Default "name" for hello().',
    )


@pytest.fixture
def hello(request):
    name = request.config.getoption("name")

    def _hello(name=None):
        if not name:
            name = request.config.getoption("name")
        return "Hello {name}!".format(name=name)

    return _hello
