from selenium import webdriver

username = "chofmanntest@gmail.com"
password = "hola1234"

driver = webdriver.Chrome("C:\\Users\\crist\\Desktop\\Cripto\\WebDrivers\\chromedriver.exe")
driver.get("https://trov.cl")
driver.set_window_size(1920, 1080)

gotologin_button = driver.find_element_by_link_text("LOGIN")
gotologin_button.click()

username_textbox = driver.find_element_by_name("email")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_name("password")
password_textbox.send_keys(password)

login_button = driver.find_element_by_id("submit-login")
login_button.submit()
