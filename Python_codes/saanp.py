from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

file_path = 'link.txt'

form_url = None

# Open the text document and read its contents
with open(file_path, 'r') as file:
    # Read the first line of the file, assuming the URL is on the first line
    form_url = file.readline().strip()
    
driver.get(form_url)
 
time.sleep(1)
 
# Data
datas = [
    ['211192 ', '190703'],
    ['211192 ', '190651'],
    ['211192 ', '22204263'],
    ['211192 ', '22105270'],
    ['211192 ', '231040620'],
    ['211192 ', '231040621'],
    ['211192 ', '231040608'],
    ['211192 ', '21204403'],
    ['211192 ', '231040406'],
    ['211192 ', '231040114'],
    ['211192 ', '231040024'],
    ['211192 ', '201121'],
    ['211192 ', '200487'],
    ['211192 ', '200794'],
    ['211192 ', '200600'],
    ['211192 ', '200244'],
    ['211192 ', '200240'],
    ['211192 ', '200037'],
    ['211192 ', '200172'],
    ['211192 ', '200106'],
    ['211192 ', '201012'],
    ['211192 ', '200645'],
    ['211192 ', '190971'],
    ['211192 ', '190221'],
    ['211192 ', '190677'],
    ['211192 ', '190775'],
    ['211192 ', '190563'],
    ['211192 ', '190446'],
    ['211192 ', '190984'],
    ['211192 ', '190137']



    
]


final = sorted(datas, key=lambda x: (x[1]))


for data in final:
    data[0], data[1] = data[1], data[0]



for data in final:
    count = 0
 
    # textboxes = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    textboxes = driver.find_elements(By.CLASS_NAME, 'whsOnd')

                      
    for textbox in textboxes:
        textbox.send_keys(data[count])
        count += 1

    # submit = driver.find_element(By.XPATH,
    #     '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    # submit.click()
    submit_button = driver.find_element(By.CLASS_NAME, 'NPEfkd')
    submit_button.click()

    submit_another_response_link = driver.find_element(By.LINK_TEXT, 'Submit another response')
    submit_another_response_link.click()
    # another_response.click()
 
driver.close()