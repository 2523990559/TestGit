from config.driver_config import DriverConfig
driver=DriverConfig().driver_config()
driver.get('http://www.tcpjwtester.top')
driver.find_element_by_xpath('地址').send_keys('用户名')
driver.find_element_by_xpath('地址').send_keys('密码')
driver.find_element_by_xpath('地址').click('111')
driver.quit()
