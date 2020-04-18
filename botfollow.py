# Created by Elivelton S.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import argparse
import os

if(len(sys.argv) < 4):
  print("Modo de usar: python %s -u usuario -s senha -p perfil"%sys.argv[0])
  print("Outro modo de uso: python %s --user usuario --pass senha --profile perfil"%sys.argv[0])
  sys.exit(0)

os.system('clear')

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--user')
parser.add_argument('-s', '--password')
parser.add_argument('-p', '--profile')

args = parser.parse_args()

class InstaBot:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.driver = webdriver.Firefox(executable_path='/home/r3tr0/Documentos/geckodriver')
    print("Carregando BOT")

  def login(self):
    print("Entrando na pagina do Instagram")
    driver = self.driver
    driver.get('https://www.instagram.com/')
    time.sleep(3)

    print("Entrando na aplicacao")
    username = driver.find_element_by_xpath('//input[@name="username"]')
    username.clear()
    username.click()
    username.send_keys(self.username)

    password = driver.find_element_by_xpath('//input[@name="password"]')
    password.clear()
    password.click()
    password.send_keys(self.password)
    password.send_keys(Keys.RETURN)
    time.sleep(3)

    self.followers(args.profile)

  def followers(self, name):
    print("Abrindo perfil alvo %s" %name)
    url = 'https://www.instagram.com/%s/' %name
    driver = self.driver
    driver.get(url)
    time.sleep(3)

    print("Carregando seguidores do perfil %s" %name)
    driver.find_element_by_xpath('//a[@class="-nal3 "]').click()
    time.sleep(2)
    for i in range(1,4):
      driver.execute_script("document.querySelector('.isgrP').scrollBy(0,document.querySelector('.isgrP').scrollHeight || document.querySelector('.isgrP').scrollHeight)", "")
      time.sleep(3)

    try:
      profiles = driver.find_elements_by_xpath("//button[contains(text(), 'Seguir')]")
      total_profiles = len(profiles)
      print("Tota de usuarios carregado: %s"%total_profiles)
      count = 0
      for profile in profiles:
        count += 1
        profile.click()
        print("Seguindo %s de %s" %(count, total_profiles))
        time.sleep(3)

    except Exception as e:
      print(e)

bot = InstaBot(args.user, args.password)
bot.login()