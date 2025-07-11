from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.reg_click = (By.LINK_TEXT, "Register")
        self.user_firstname = (By.ID, "customer.firstName")
        self.user_lastname = (By.XPATH, "//tbody/tr[2]/td[2]/input")
        self.user_street = (By.NAME, "customer.address.street")
        self.user_city = (By.ID, "customer.address.city")
        self.user_name = (By.ID, "customer.username")
        self.user_password = (By.ID, "customer.password")
        self.user_re_enter_pwd = (By.ID, "repeatedPassword")
        self.cust_state = (By.ID, "customer.address.state")
        self.cust_zip = (By.ID, "customer.address.zipCode")
        self.cust_ph_no = (By.ID, "customer.phoneNumber")
        self.cust_ssn = (By.ID, "customer.ssn")
        self.reg_click_btn = (By.XPATH, "//input[@value='Register']")


    def register(self,firstname,lastname,street,city,user_name,password,re_enter,state,zip,ph_no,ssn):
        self.driver.find_element(*self.reg_click).click()
        self.driver.find_element(*self.user_firstname ).send_keys(firstname)
        self.driver.find_element(*self.user_lastname).send_keys(lastname)
        self.driver.find_element(*self.user_street).send_keys(street)
        self.driver.find_element(*self.user_city ).send_keys(city)
        self.driver.find_element(*self.user_name).send_keys(user_name)
        self.driver.find_element(*self.user_password).send_keys(password)
        self.driver.find_element(*self.user_re_enter_pwd).send_keys(re_enter)
        self.driver.find_element(*self.cust_state).send_keys(state)
        self.driver.find_element(*self.cust_zip ).send_keys(zip)
        self.driver.find_element(*self.cust_ph_no).send_keys(ph_no)
        self.driver.find_element(*self.cust_ssn).send_keys(ssn)
        self.driver.find_element(*self.reg_click_btn).click()
