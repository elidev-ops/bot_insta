# Created by Elivelton S.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
import os
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-p', '--password')
parser.add_argument('-t', '--tag')

args = parser.parse_args()

class instagramBot:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.drive = webdriver.Firefox(executable_path='/home/r3tr0/Documentos/geckodriver')

  def login(self):
    driver = self.drive
    driver.get('https://www.instagram.com/')
    time.sleep(3)

    username = driver.find_element_by_xpath("//input[@name='username']")
    password = driver.find_element_by_xpath("//input[@name='password']")
    username.clear()
    username.click()
    username.send_keys(self.username)

    password.clear()
    password.click()
    password.send_keys(self.password)
    password.send_keys(Keys.RETURN)

    time.sleep(3)

    self.likePost(args.tag)

  def likePost(self, hashtag):
    driver = self.drive
    driver.get('https://www.instagram.com/explore/tags/'+ hashtag +'/')

    time.sleep(3)
    
    for i in range(1,3):
      driver.execute_script("window.scrollBy(0,document.body.scrollHeight || document.documentElement.scrollHeight)", "")
      time.sleep(3)

    divs = driver.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']")
    hrefs = [elem.find_element_by_xpath(".//a[@href]") for elem in divs]
    
    pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
    [href for href in pic_hrefs if hashtag in href]
    print("Na #"+ hashtag + ' tem ' + str(len(pic_hrefs)) + ' links')
    count = 0
    for pic_href in pic_hrefs:
      driver.get(pic_href)
      driver.execute_script("window.scrollBy(0,document.body.scrollHeight || document.documentElement.scrollHeight)", "")
      try:
        count += 1
        driver.find_element_by_xpath("//button[@class='wpO6b ']").click()
        print("Curtindo: %s de %s publicacoes" %(count, str(len(pic_hrefs))))
        time.sleep(19)
      except Exception as e:
        print(e)
        time.sleep(3)

bot = instagramBot(args.user, args.password)
bot.login()