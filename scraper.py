'''

'''   

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
class Scraper:
    
    def __init__(self):
        self.url = "https://www.screwfix.com"
        self.driver = webdriver.Chrome()
        self.sub_category_list = []
        self.product_links_list = []
        self.product_features_table = []
    
    def open_url(self):
        self.driver.get(self.url)
    
    def cookies_check(self):
        accept_cookies = self.driver.find_element(by=By.XPATH, value='//a[text()="Accept Cookies"]')
        print("Found!")

    def initial_search(self, search_item):
        # Search for item
        search_bar = self.driver.find_element(by=By.XPATH, value='//*[@id="keyword-search"]')
        search_bar.send_keys(search_item)
        search_bar.send_keys(Keys.RETURN)

    def get_sub_category_list(self):
        try:
            sub_category_top_webelement = self.driver.find_element(by=By.XPATH, value='//ul[@class="n ln__cats"]')
        except:
            return

        sub_category_individual_name_webelements = sub_category_top_webelement.find_elements(By.XPATH, value='.//span[@class="ln__facet"]')
        sub_category_individual_names_list = [i.text for i in sub_category_individual_name_webelements]
        sub_category_individual_link_webelements = sub_category_top_webelement.find_elements(By.XPATH, value='.//a')
        sub_category_individual_links_list = [i.get_attribute('href') for i in sub_category_individual_link_webelements]
        self.sub_category_list = list(zip(sub_category_individual_names_list, sub_category_individual_links_list))

    def get_sub_category_choice(self):
        if not self.sub_category_list:
            return
        else:
            print("Your search term gave multiple sub-categories as a result.")
            for i in self.sub_category_list:
                print(i)
            sub_category_choice = input("Please select from them to continue")
            self.driver.get(self.sub_category_list[int(sub_category_choice)][1])

    def get_product_links(self):
        # Get links to individual products 
        product_links_webelement = self.driver.find_element(By.XPATH, value='//div[@class="row flex-container"]')
        product_links_individual_webelements = product_links_webelement.find_elements(By.XPATH, value='.//div[@class="lii__product-details"]')
        self.product_links_list = [i.find_element(By.XPATH, value='.//a').get_attribute('href') for i in product_links_individual_webelements]
    
    def get_product_features_table(self):
        # Get table of product features
        for i in self.product_links_list:
            self.driver.get(i)
            time.sleep(10)
            specifications_tab=self.driver.find_element(By.XPATH, value='//a[@href="#product_additional_details_container"]')
            specifications_tab.send_keys("")
            specifications_tab.send_keys(Keys.ENTER)
            time.sleep(1)
            
            product_name=self.driver.find_element(By.XPATH,value='//h1[@id="product_description"]').text
            product_price_webelement=self.driver.find_element(By.XPATH,value='//input[contains(@id,"analytics_prodPrice_")]')
            product_features_items_webelement_list=self.driver.find_elements(By.XPATH,value='//td[contains(@id,"product_selling_attribute_name")]')
            product_features_values_webelement_list=self.driver.find_elements(By.XPATH,value='//td[contains(@id,"product_selling_attribute_value")]')

            self.product_features_table.append([product_name,"Price",product_price_webelement.get_attribute('value')])
            for i, j in zip(product_features_items_webelement_list, product_features_values_webelement_list):
                self.product_features_table.append([product_name, i.text, j.text])
    
    def transform_product_table(self):

        product_features_set = set()
        product_names_set = set()

        for i in self.product_features_table:
            product_features_set.add(i[1])

        for i in self.product_features_table:
            product_names_set.add(i[0])

        product_features_list = []
        for i in product_features_set:
            product_features_list.append(i)
        
        product_names_list = []
        for i  in product_names_set:
            product_names_list.append(i)

        rows = []
        for i in product_names_list:
            new_row = [i]
            for j in product_features_list:
                found = False
                for k in self.product_features_table:
                    if i==k[0] and j==k[1]:
                        new_row.append(k[2])
                        found = True
                        break
                if not found:
                    new_row.append("N/A")
            rows.append(new_row)
        product_features_list.insert(0,"")

        with open("scraped-data.csv", "w") as f:
            write = csv.writer(f)
            write.writerow(product_features_list)
            write.writerows(rows)
        

        

def main():                                                                   
    scraper = Scraper()
    scraper.open_url()
    time.sleep(10)
    #scraper.cookies_check()
    #time.sleep(10)
    scraper.initial_search("drill")
    time.sleep(10)
    scraper.get_sub_category_list()
    time.sleep(10)
    scraper.get_sub_category_choice()
    time.sleep(10)
    scraper.get_product_links()
    time.sleep(10)
    scraper.get_product_features_table()
    scraper.transform_product_table()

if __name__=='__main__':
    main()


