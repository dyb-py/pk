import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.interaction import KEY
from selenium.webdriver.common.keys import Keys

driver = selenium.webdriver.Chrome()
driver.switch_to.window()
driver.forward()
action = ActionChains(driver).key_down(Keys.CONTROL())

