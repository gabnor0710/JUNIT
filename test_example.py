import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_title(browser):
    browser.get('https://www.google.com')
    assert browser.title == 'Google'


if __name__ == '__main__':
    pytest.main(args=['--junitxml=report.xml'])