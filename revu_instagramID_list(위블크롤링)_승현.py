{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "신청자 페이지 url을 입력\n",
      "https://www.revu.net/campaign/257918/applicant\n",
      "저장파일명을 입력하세요\n",
      "wow\n"
     ]
    },
    {
     "ename": "WebDriverException",
     "evalue": "Message: Failed to decode response from marionette\n",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-67-a9cbd9b1ac27>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     63\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     64\u001b[0m             \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 65\u001b[0;31m             \u001b[0mig_url\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_element_by_xpath\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'//*[@id=\"ng-app\"]/body/root/div/ng-transclude/ng-view/mypage-review/div/div/div[1]/aside-snb/aside/aside-me/section/div/div[4]/a'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_attribute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'href'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     66\u001b[0m             \u001b[0mreal_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mid_check\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mig_url\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     67\u001b[0m             \u001b[0mdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mig_url\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m//anaconda3/lib/python3.7/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mfind_element_by_xpath\u001b[0;34m(self, xpath)\u001b[0m\n\u001b[1;32m    392\u001b[0m             \u001b[0melement\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_element_by_xpath\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'//div/td[1]'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    393\u001b[0m         \"\"\"\n\u001b[0;32m--> 394\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_element\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mby\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mXPATH\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mxpath\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    395\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    396\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mfind_elements_by_xpath\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mxpath\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m//anaconda3/lib/python3.7/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mfind_element\u001b[0;34m(self, by, value)\u001b[0m\n\u001b[1;32m    976\u001b[0m         return self.execute(Command.FIND_ELEMENT, {\n\u001b[1;32m    977\u001b[0m             \u001b[0;34m'using'\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mby\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 978\u001b[0;31m             'value': value})['value']\n\u001b[0m\u001b[1;32m    979\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    980\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mfind_elements\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mby\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mID\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m//anaconda3/lib/python3.7/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    319\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    320\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 321\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    322\u001b[0m             response['value'] = self._unwrap_value(\n\u001b[1;32m    323\u001b[0m                 response.get('value', None))\n",
      "\u001b[0;32m//anaconda3/lib/python3.7/site-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    240\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'alert'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'text'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    241\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 242\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    243\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    244\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_value_or_default\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdefault\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mWebDriverException\u001b[0m: Message: Failed to decode response from marionette\n"
     ]
    }
   ],
   "source": [
    "from lxml import html\n",
    "from selenium import webdriver\n",
    "from bs4 import BeautifulSoup\n",
    "from selenium.common.exceptions import NoSuchElementException       \n",
    "import time\n",
    "import pandas as pd\n",
    "from datetime import datetime\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.common.action_chains import ActionChains\n",
    "from selenium.webdriver.common.alert import Alert\n",
    "import random\n",
    "import os\n",
    "import requests\n",
    "import timeit\n",
    "\n",
    "def id_check(link):\n",
    "    \n",
    "    id_start = link.find(\"m/\")\n",
    "    id_start += 2\n",
    "    applicant_id = link[id_start:len(link)]\n",
    "\n",
    "    return applicant_id\n",
    "\n",
    "\n",
    "print('신청자 페이지 url을 입력')\n",
    "site_url = input()\n",
    "# print('최소 일일 방문자 평균 입력')\n",
    "# minimum =int(input())\n",
    "\n",
    "print('저장파일명을 입력하세요')\n",
    "name=input()\n",
    "review_df=pd.DataFrame(columns=['지원자','id','팔로워수'])\n",
    "start = timeit.default_timer()\n",
    "\n",
    "driver=webdriver.Firefox(executable_path='./geckodriver')\n",
    "driver.get(site_url)\n",
    "time.sleep(1)\n",
    "html = driver.page_source\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "applicant=[]\n",
    "ig_id=[]\n",
    "follow_list=[]\n",
    "a=1\n",
    "instagram_num = []\n",
    "total = int(driver.find_element_by_xpath('//*[@id=\"ng-app\"]/body/root/div/ng-transclude/ng-view/campaign-new/div/div/div[1]/div/campaign-new-applicant-list/div[1]/campaign-new-tabs/div/ul/li[2]/a/span/strong').text)\n",
    "while True:\n",
    "    try:\n",
    "        time.sleep(1)\n",
    "        driver.find_element_by_xpath('//*[@id=\"ng-app\"]/body/root/div/ng-transclude/ng-view/campaign-new/div/div/div[1]/div/campaign-new-applicant-list/div[1]/div[3]/ul/div[2]/button').click()\n",
    "    except NoSuchElementException:\n",
    "            break\n",
    "            \n",
    "while total != a-1:\n",
    "\n",
    "    try:\n",
    "        \n",
    "        applicant_id = driver.find_element_by_xpath('//*[@id=\"ng-app\"]/body/root/div/ng-transclude/ng-view/campaign-new/div/div/div[1]/div/campaign-new-applicant-list/div[1]/div[3]/ul/li[{}]/div/div/span'.format(a)).text\n",
    "        new_url = driver.find_element_by_xpath('//*[@id=\"ng-app\"]/body/root/div/ng-transclude/ng-view/campaign-new/div/div/div[1]/div/campaign-new-applicant-list/div[1]/div[3]/ul/li[{}]/a'.format(a)).get_attribute('href')\n",
    "        driver.execute_script('''window.open(\"about:blank\", \"_blank\");''')\n",
    "        driver.switch_to.window(driver.window_handles[1])\n",
    "        driver.get(new_url)\n",
    "        try:  \n",
    "            time.sleep(1)\n",
    "            ig_url = driver.find_element_by_xpath('//*[@id=\"ng-app\"]/body/root/div/ng-transclude/ng-view/mypage-review/div/div/div[1]/aside-snb/aside/aside-me/section/div/div[4]/a').get_attribute('href')\n",
    "            real_id = id_check(ig_url)\n",
    "            driver.get(ig_url)\n",
    "            follow_num = driver.find_element_by_xpath('//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a/span').get_attribute('title')\n",
    "            follow_num = int(filter(str.isdigit, temp_follow_num))\n",
    "            follow_list.append(follow_num)\n",
    "            applicant.append(applicant_id)\n",
    "            ig_id.append(real_id)\n",
    "        except NoSuchElementException:\n",
    "            a+=1\n",
    "            driver.close()\n",
    "            driver.switch_to.window(driver.window_handles[0])\n",
    "            continue\n",
    "        driver.close()\n",
    "        driver.switch_to.window(driver.window_handles[0])\n",
    "        a += 1\n",
    "        print(a, applicant_id)\n",
    "    except NoSuchElementException:\n",
    "        break\n",
    "    time.sleep(1)\n",
    "    \n",
    "    \n",
    "\n",
    "final=zip(applicant,ig_id,follow_list)\n",
    "for i in final:\n",
    "    ap_id = i[0]\n",
    "    instagram=i[1]\n",
    "    number =i[2]\n",
    "    review_df = review_df.append(pd.DataFrame([[ap_id,instagram,number]], columns=['지원자','id','팔로워수']))\n",
    "review_df.to_excel('{}.xlsx'.format(name),index=False)\n",
    "stop = timeit.default_timer()\n",
    "print('Time: ', stop - start)\n",
    "print(\"DONE\")\n",
    "driver.close()\n",
    "\n",
    "\n",
    " \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
