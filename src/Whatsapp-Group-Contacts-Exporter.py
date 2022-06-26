from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def main():
    grp_name = input("Enter group name\n")
    driver_path = "../WebDriver/chromedriver"
    options = Options()
    options.add_argument('user-data-dir=./User_Data')
    driver = webdriver.Chrome(executable_path = driver_path, chrome_options=options)
    driver.get("https://web.whatsapp.com/")
    input("Scan the QR code to login to whatsapp web and press enter on sucessful login\n")
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]').send_keys(grp_name)
    driver.find_element_by_xpath("//span[@title='"+grp_name+"']").click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header/div[2]').click()
    grp_members_info = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/section/div[6]/div[1]/div/div/div[1]')
    print(f"Group Members: {grp_members_info.text}")
    grp_members_info.click()
    for i in range(2,11):
        print(i)
        #print(driver.find_element_by_xpath(f).text)
        print(driver.find_element(by=By.XPATH, value=f'/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/div[2]/div/div/div/div[{i}]/div/div/div[2]/div[1]/div/span').text)
        print("-"*50)
    input()
    

if __name__ == "__main__":
    main()
 
