import unittest
from selenium import webdriver
import chromedriver_autoinstaller
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage
from pages.create_account_page import CreateAccountPage
from pages.newsletter_page import NewsLetterPage
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By


class FinalProject(unittest.TestCase):
    def setUp(self) -> None:
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.get('http://automationpractice.com/index.php')
        # WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')))

    def test_createAccountFail(self):
        TC = HomePage(self.driver)
        TC.wait(10)

        TC.click_sigin_btn()

        TC = SignInPage(self.driver)
        TC.enter_email_addr('dgdghfd@gmail.com')
        TC.click_create_btn()

    def test_createAcountSuccess(self):
        TC = HomePage(self.driver)
        TC.wait(10)
        TC.click_sigin_btn()
        TC.wait(10)

        TC = SignInPage(self.driver)
        TC.enter_email_addr('gfgdfga@gmail.com')
        TC.click_create_btn()

        TC = CreateAccountPage(self.driver)
        TC.wait(10)
        TC.click_value()
        TC.enter_value('nguyen', 'minh', 'Truongminh1990', 'abc', 'hoang', 'lqa', '36 Nguyen Co Thach', '37 Tay Tuu',
                       'HA NOI', '10000', 'abcd', '01928377466', '090398772643')
        TC.click_button()
        TC.result_mess()

    def test_submit_newsletter(self):
        TC = NewsLetterPage(self.driver)
        TC.wait(10)
        TC.enter_email('sreegg@gmail.com')
        TC.click_submit()
        TC.display_mess()



    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
