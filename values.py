import os
from selenium import webdriver
from fake_useragent import UserAgent
from fake_useragent import FakeUserAgentError


# Login Account
# Email = os.environ.get("EMAIL")
# Password = os.environ.get("PASSWORD")
# Website logger
Website_url = "https://siswa.smktelkom-mlg.sch.id"
Website_url_absen = "https://siswa.smktelkom-mlg.sch.id/presnow"
Website_key = "6Lc7NmoUAAAAAJAgPU2_TypLL0H1UG_Fj9vUMl3O"
Captcha_api = "f363822ea4b23addabb0a1d6b3e537c9"

# =====================================
# DON'T CHANGE THIS SETUP!
# def account():
#     return Email, Password

def sitelogger():
    return Website_url, Website_key, Captcha_api, Website_url_absen

def browser():
    try:
        ua = UserAgent()
    except FakeUserAgentError:
        pass

    chromes = webdriver.ChromeOptions()
    chromes.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chromes.add_argument(f"user-agent={ua.random}")
    chromes.add_argument("--headless")
    chromes.add_argument("--no-sandbox")
    chromes.add_argument("--disable-dev-sh-usage")

    # Release
    # browser = webdriver.Chrome(executable_path=os.environ.get(
    #     "CHROMEDRIVER_PATH"), chrome_options=chromes)

    ## Development
    browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=chromes)
    
    return browser