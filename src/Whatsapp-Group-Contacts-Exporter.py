from selenium import webdriver

def main():
    driver_path = "../WebDriver/chromedriver"
    driver = webdriver.Chrome(executable_path = driver_path)
    driver.get("https://web.whatsapp.com/")
    input("Login to whatsapp web and press enter to continue")

if __name__ == "__main__":
    main()
 
