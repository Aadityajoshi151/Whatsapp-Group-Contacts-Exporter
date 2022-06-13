from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    grp_name = input("Enter Group/Chat name\n")
    driver_path = "../WebDriver/chromedriver"
    options = Options()
    options.add_argument('user-data-dir=./User_Data')
    driver = webdriver.Chrome(executable_path = driver_path, chrome_options=options)
    driver.get("https://web.whatsapp.com/")
    input("Login to whatsapp web and press enter to continue")
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]').send_keys(grp_name)
    input()

if __name__ == "__main__":
    main()
 
