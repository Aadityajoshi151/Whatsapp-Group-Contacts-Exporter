from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    grp_name = input("Enter group name\n")
    driver_path = "../WebDriver/chromedriver"
    options = Options()
    options.add_argument('user-data-dir=./User_Data')
    driver = webdriver.Chrome(executable_path = driver_path, chrome_options=options)
    driver.get("https://web.whatsapp.com/")
    input("Scan the QR code to login to whatsapp web and press enter on sucessfull login\n")
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]').send_keys(grp_name)
    driver.find_element_by_xpath("//span[@title='"+grp_name+"']").click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header/div[2]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/section/div[6]/div[1]/div/div/div[1]').click()
    input()

if __name__ == "__main__":
    main()
 
