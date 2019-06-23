from pages.login import login
import pytest
from  data.Testdata import *

# Launching the browser and go into the login sites
@pytest.mark.usefixtures("test_setup")
class Test_Acttime:
    def test_loginact(self):
        driver=self.driver
        time=login(driver)
        time.loginactime(USERNAME,PASSWORD)



# home page logut
# def test_logoutact():
#        driver.find_element_by_id("logoutLink").click()



