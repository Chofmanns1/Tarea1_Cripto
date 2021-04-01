from selenium import webdriver

email = input("Ingrese un correo: ")
#password = input("Ingrese una contraseña: ")
#firstname = input("Ingrese un nombre: ")
#lastname = input("Ingrese un apellido: ")
#birthdate = input("Ingrese fecha de nacimiento (YYYY-MM-DD): "

password = "asdasd"
firstname = "jorge"
lastname = "juanes"
birthdate = "1990-05-05"

driver = webdriver.Chrome("C:\\Users\\crist\\Desktop\\Cripto\\WebDrivers\\chromedriver.exe")
driver.get("https://trov.cl")
driver.set_window_size(1920, 1080)

gotologin_button = driver.find_element_by_link_text("LOGIN")
gotologin_button.click()

gotoCreate_button = driver.find_element_by_link_text("¿No tiene una cuenta? Crear una aquí")
gotoCreate_button.click()

#socialTitle_checkbox = driver.find_element_by_link_text("Sr.")
#socialTitle_checkbox.click()

firstname_textbox = driver.find_element_by_name("firstname")
firstname_textbox.send_keys(firstname)

lastname_textbox = driver.find_element_by_name("lastname")
lastname_textbox.send_keys(lastname)

email_textbox = driver.find_element_by_name("email")
email_textbox.send_keys(email)

password_textbox = driver.find_element_by_name("password")
password_textbox.send_keys(password)

birthdate_textbox = driver.find_element_by_name("birthday")
birthdate_textbox.send_keys(birthdate)

save_button = driver.find_element_by_name("submitCreate")
save_button.submit()