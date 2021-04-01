from selenium import webdriver

#email = input("Ingrese el correo: ")
email = "chofmanntest@gmail.com"

driver = webdriver.Chrome("C:\\Users\\crist\\Desktop\\Cripto\\WebDrivers\\chromedriver.exe")
driver.get("https://trov.cl")
driver.set_window_size(1920, 1080)

gotologin_button = driver.find_element_by_link_text("LOGIN")
gotologin_button.click()

gotoCreate_button = driver.find_element_by_link_text("¿Olvidó su contraseña?")
gotoCreate_button.click()

email_textbox = driver.find_element_by_name("email")
email_textbox.send_keys(email)

send_button = driver.find_element_by_name("submit")
send_button.click()
