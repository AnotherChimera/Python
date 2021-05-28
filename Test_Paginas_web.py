import unittest
import time

from selenium import webdriver
unittest.TestLoader.sortTestMethodsUsing = None

class pruebasSelenium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()

    def test_ingresar_nombre(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
        time.sleep(2)
        input_nombre = driver.find_element_by_id("user-message")
        input_nombre.send_keys("Armando Padilla")
        time.sleep(2)
        boton_nombre = driver.find_element_by_xpath("//button[contains(text(),'Show Message')]")
        boton_nombre.click()
        valor_nombre=driver.find_element_by_xpath("//span[@id='display']")
        print("Valor ingresado " + input_nombre.text)
        self.assertEqual(valor_nombre.text, "Armando Padilla")
        time.sleep(2)

    def test_checkbox_demo(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
        time.sleep(2)
        input_check = driver.find_element_by_xpath("//input[@id='isAgeSelected']")
        input_check.click()
        valor_succes_check=driver.find_element_by_xpath("//div[@id='txtAge']")
        self.assertEqual(valor_succes_check.text, "Success - Check box is checked")
        time.sleep(2)

    def test_radio_button_demo(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")
        time.sleep(2)
        input_radio_masculino = driver.find_element_by_xpath("//body/div[@id='easycont']/div[1]/div[2]/div[1]/div[2]/label[1]")
        input_radio_masculino.click()
        button_ok=driver.find_element_by_xpath("//button[@id='buttoncheck']")
        button_ok.click()
        texto_masculino = driver.find_element_by_css_selector\
            ("div.container-fluid.text-center:nth-child(2) div.row div.col-md-6.text-left:nth-child(2) div.panel.panel-default:nth-child(4) div.panel-body > p.radiobutton:nth-child(7)")
        print("El radiobutton seleccionado es " + texto_masculino.text)
        # self.assertEqual(texto_masculino.text, "Success - Check box is checked")
        self.assertEqual(texto_masculino.text, "Radio button 'Male' is checked")
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()

