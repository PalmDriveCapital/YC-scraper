from selenium import webdriver
import time
import pandas as pd
import batch
import scroller
USE_JSON = False

def main():
    search_query = 'https://www.ycombinator.com/companies/' + batch.command_line()

    driver = webdriver.Chrome(executable_path='C:\\Users\\Kyle\\Downloads\\chromedrivers\\chromedriver.exe')
    company_information = []
    founder_information = []
    driver.get(search_query)
    time.sleep(5)

    # Scroll to the bottom of page
    scroller.scroll(driver)

    company_list = driver.find_elements_by_class_name("styles-module__company___1UVnl")
    company_industries_array = []
    company_counter = 1
    
    for each_company in company_list:
        # Getting company info
        company_name = each_company.find_elements_by_class_name("styles-module__coName___3zz21")[0]
        company_location = each_company.find_elements_by_class_name("styles-module__coLocation___yhKam")[0]
        company_YC_batch = each_company.find_elements_by_class_name("styles-module__pill___1Cdn5")[0]
        company_industries_array.append(industries(each_company, company_counter))
        company_counter += 1
        # Get information from new tab
        information_from_new_tab = switch_tabs(driver, company_name)
        company_YC_profile, company_domain = information_from_new_tab[0], information_from_new_tab[1]
        # Saving company info 
        company_info = [company_name.text, company_location.text, company_YC_profile, company_domain, company_YC_batch.text, ", ".join(company_industries_array[company_counter - 2])]
        # Saving into company_information
        company_information.append(company_info)
        founder_information.append(information_from_new_tab[2])
    driver.quit()

    company_information_df = pd.DataFrame(company_information)
    company_information_df.columns = ['Company', 'Location', 'YC Profile Page', 'Domain Name', 'YC Batch', 'Industries']
    founder_information_df = pd.DataFrame(founder_information)

    # Set USE_JSON to True if want JSON  
    if USE_JSON:
        company_information_df.to_json('company_information.json')
        founder_information_df.to_json('founder_information.json')
    else:
        company_information_df.to_csv('company_information.csv', index=False)
        founder_information_df.to_csv('founder_information.csv', index=False)
    
def industries(each_company, company_counter):
    industry_counter = 2
    # Industry HTML page location
    industries_page_location = "/html/body/div[1]/section/div/div/div[2]/div[4]/a[" + str(company_counter) + "]/div[2]/div[3]/span[" + str(industry_counter) + "]"
    each_company_industries_array = []
    # While there are still industries for a company
    while (len(each_company.find_elements_by_xpath(industries_page_location)) > 0):
        company_industries = each_company.find_elements_by_xpath(industries_page_location)[0]
        # Append new industry to company
        each_company_industries_array.append(company_industries.text)
        # Update industry counter, update new industry HTML page location
        industry_counter +=1
        industries_page_location = "/html/body/div[1]/section/div/div/div[2]/div[4]/a[" + str(company_counter) + "]/div[2]/div[3]/span[" + str(industry_counter) + "]"
    return each_company_industries_array

def switch_tabs(driver, company_name):
    # Set current window as main_window
    main_window = driver.current_window_handle
    # Open YC profile tab of company
    company_name.click()
    time.sleep(1) 
    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != main_window:
            driver.switch_to.window(window_handle)
            # Update company_YC_profile and company_domain URLs
            company_YC_profile = driver.current_url
            company_domain = driver.find_element_by_class_name("main-column").find_element_by_class_name("links").find_element_by_tag_name("a").get_property("href")
            founder_info = founder_profile(driver)
            break
    # Close new tab and switch back to YC companies list tab
    driver.close()
    driver.switch_to.window(main_window)
    # Put information from new tab into an array
    information_from_new_tab = [company_YC_profile, company_domain, founder_info]
    return information_from_new_tab

def founder_profile(driver):
    founder_info = []

    founder_counter = 1

    founder_name_page_location = '/html/body/div[1]/section[2]/div[' + str(founder_counter) + ']/div[1]/h3'
    founder_name_side_location = '/html/body/div[1]/section[2]/div/div[' + str(founder_counter) + ']/div/div/div[1]'
    founder_profile_location = '/html/body/div[1]/section[2]/div[' + str(founder_counter) + ']/div[1]/p'

    company_name = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div[1]/div[2]/h1')
    founder_info.append(company_name.text)
    # If founder name in profile page, take from there, otherwise take from social media link
    if (len(driver.find_elements_by_xpath(founder_name_page_location)) > 0):
        while(len(driver.find_elements_by_xpath(founder_name_page_location)) > 0):
            founders = driver.find_elements_by_xpath(founder_name_page_location)[0]
            founder_profile = driver.find_elements_by_xpath(founder_profile_location)[0]
            founder_info.append(founders.text)
            founder_info.append(founder_profile.text)
            # Update page location
            founder_counter += 1
            founder_name_page_location = '/html/body/div[1]/section[2]/div[' + str(founder_counter) + ']/div[1]/h3'
            founder_profile_location = '/html/body/div[1]/section[2]/div[' + str(founder_counter) + ']/div[1]/p'
    else:
        while(len(driver.find_elements_by_xpath(founder_name_side_location)) > 0):
            founders = driver.find_elements_by_xpath(founder_name_side_location)[0]
            founder_info.append(founders.text)
            # Update page location
            founder_counter +=1
            founder_name_side_location = '/html/body/div[1]/section[2]/div/div[' + str(founder_counter) + ']/div/div/div[1]'
    return founder_info

# Run main
main()