# %%
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup
from pprint import pprint

# ninja: "https://etherscan.io/token/generic-tokenholders2?m=normal&a=0x3d6ab55fb262f786ba1e9d1172657fb2d462f1f8&s=4888&sid=a5e725b7d995bd31ed47079822a56b4c"
# sloth: "https://etherscan.io/token/generic-tokenholders2?m=normal&a=0xb183858f744eeff5c86f716b7e93d15a8696fa9a&s=889&sid=adf6ba12a50546cc51844facdcfc46cf"

### params
URL = "https://etherscan.io/token/generic-tokenholders2?m=normal&a=0x3d6ab55fb262f786ba1e9d1172657fb2d462f1f8&s=4888&sid=a5e725b7d995bd31ed47079822a56b4c"
LOWER_BOUND = 10
DRIVER_NAME = './chromedriver'
###


def crawl():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(DRIVER_NAME, options=options)
    p = 1
    datas = []
    while True:
        print("page: {0}".format(p))
        driver.get("{0}&p={1}".format(URL, p))
        table = driver.find_element_by_tag_name('table')
        for tr in table.find_elements_by_tag_name("tr"):
            tmp_row = tr.find_elements_by_tag_name("td")
            if(len(tmp_row)!=4):
                continue
            addr = tmp_row[1].find_element_by_tag_name("a").text
            quan = tmp_row[2].text
            if(int(quan) < LOWER_BOUND):
                return datas
            datas.append((addr, quan))
        p += 1

datas = crawl()
# %%
# write the result to file
import pandas as pd
dict_data = {"address":[d[0] for d in datas], "quantity":[d[1] for d in datas]}
df = pd.DataFrame(dict_data)
df.to_csv("holders.csv", index=False)
