{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "키워드를 입력하세요: \n",
      "하\n",
      "읽을 파일명을 입력하세요: \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import time\n",
    "import os\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.support.ui import WebDriverWait\n",
    "from selenium.webdriver.support import expected_conditions as EC\n",
    "from selenium.common.exceptions import NoSuchElementException\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.support.ui import Select\n",
    "from datetime import date, datetime, timedelta\n",
    "from pytz import timezone\n",
    "\n",
    "def extract_id(blog_url):\n",
    "    if \"?\" in blog_url:\n",
    "        blog_end = blog_url.find('?',15)\n",
    "    elif \"naver.com/\" in blog_url:\n",
    "        blog_end = blog_url.find('/', 15)\n",
    "    elif \".me/\" in blog_url:\n",
    "        blog_end=blog_url.find(\"me/\")\n",
    "        blog_end += 3\n",
    "    else:\n",
    "        blog_end = 1\n",
    "    blog = blog_url[0:blog_end]\n",
    "    if \".com/\" in blog:\n",
    "        blog_id_begin = blog.find(\"com/\")\n",
    "        blog_id_begin += 4\n",
    "        blog_id_end = len(blog)\n",
    "    else:\n",
    "        blog_id_begin =0\n",
    "        blog_id_end = blog.find(\".blog\")\n",
    "    blog_id=blog[blog_id_begin:blog_id_end]\n",
    "    return blog_id\n",
    "\n",
    "\n",
    "print('키워드를 입력하세요: ')\n",
    "keyword = input()\n",
    "print('읽을 파일명을 입력하세요: ')\n",
    "filename = input()\n",
    "print('쓸 파일명을 입력하세요: ')\n",
    "name = input()\n",
    "name1 = name\n",
    "\n",
    "source = \"https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query={}&sm=tab_pge&srchby=all&st=sim&where=post&start=1\".format(keyword)\n",
    "temp = source[0:len(source)-1]\n",
    "driver=webdriver.Firefox(executable_path='./geckodriver')\n",
    "time.sleep(5)\n",
    "filename = './'+filename +'.xlsx'\n",
    "\n",
    "df = pd.read_excel(filename)\n",
    "\n",
    "\n",
    "id_list = []\n",
    "page_n_list = []\n",
    "rank_list = []\n",
    "try:\n",
    "    for i in df.itertuples():\n",
    "        print(i)\n",
    "        driver.get(source)\n",
    "        item_number=1\n",
    "        a=1\n",
    "        page_n = 1\n",
    "        rank_in_page = 1\n",
    "        ID = i[1]\n",
    "        id_list.append(ID)\n",
    "        while True:\n",
    "            try:\n",
    "                blog_url_temp = driver.find_element_by_xpath('//*[@id=\"sp_blog_{}\"]/dl/dd[3]/span/a[2]'.format(a)).get_attribute('href')\n",
    "                blog_url = blog_url_temp[8:len(blog_url_temp)]\n",
    "                temp_id = extract_id(blog_url)\n",
    "                print(a)\n",
    "                if ID == temp_id:\n",
    "                    print(temp_id)\n",
    "                    page_n_list.append(page_n)\n",
    "                    rank_list.append(a)\n",
    "                    break\n",
    "                else:\n",
    "                    a += 1\n",
    "                    continue\n",
    "            except NoSuchElementException: \n",
    "                a = 1\n",
    "                page_n += 1\n",
    "                item_number += 10\n",
    "                source_temp = temp + str(item_number)\n",
    "                driver.get(source_temp)\n",
    "                time.sleep(1)\n",
    "                print('다음페이지')\n",
    "               \n",
    "except ValueError:\n",
    "    print('끝')\n",
    "\n",
    "print('끝')\n",
    "review_df=pd.DataFrame(columns=['아이디','페이지수','순위'])\n",
    "final=zip(id_list,page_n_list, rank_list)\n",
    "for i in final:\n",
    "    applicantcount = i[0]\n",
    "    pagecount=i[1]\n",
    "    rankcount=i[2]\n",
    "    \n",
    "    review_df = review_df.append(pd.DataFrame([[applicantcount,pagecount,rankcount]], columns=['아이디','페이지수','순위']))\n",
    "review_df.to_excel('{}.xlsx'.format(name1),index=False)\n",
    "\n",
    "\n"
   ]
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
