from selenium import webdriver

# GLOBAL - STATIC VARIABLES:
DIRECTORY = "C:\\Users\\Anjaniy\\PycharmProjects\\AmazonPriceTracker\\reports"
NAME = str(input('Which Product Do You Wish To Look For ? \n'))
CURRENCY = '€'
MIN_PRICE = str(input('What Should Be The Minimum Price In € ? \n'))
MAX_PRICE = str(input('What Should Be The Maximum Price In € ? \n'))
FILTERS = {
    'min': MIN_PRICE,
    'max': MAX_PRICE
}
# BASE_URL:
BASE_URL = 'http://www.amazon.de/'


# GET THE CHROME_DRIVER:
def get_chrome_web_driver(options):
    return webdriver.Chrome('./chromedriver', chrome_options=options)


#  GET THE CHROME_OPTIONS:
def get_chrome_options():
    return webdriver.ChromeOptions()


# FUNCTION FOR IGNORE THE CERTIFICATE ERRORS:
def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')


# FUNCTION FOR INCOGNITO_CHROME:
def set_browser_as_incognito(options):
    options.add_argument('--incognito')


def set_automation_as_head_less(options):
    options.add_argument('--headless')
