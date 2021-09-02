{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "from lxml import html\n",
    "import requests\n",
    "\n",
    "# link = \"http://blog.naver.com/NVisitorgp4Ajax.nhn?blogId=chloepark472\"\n",
    "# driver=webdriver.Firefox(executable_path='./geckodriver')\n",
    "# driver.get(link)\n",
    "\n",
    "# xml = driver.page_source\n",
    "# soup = BeautifulSoup(xml, 'html.parser')\n",
    "\n",
    "# n = soup.select(\".cnt\")\n",
    "\n",
    "\n",
    "link = \"http://blog.naver.com/NVisitorgp4Ajax.nhn?blogId=chloepark472\"\n",
    "f = requests.get(link)\n",
    "# tree = html.fromstring(f.content)\n",
    "script = f.text\n",
    "\n",
    "lines = script.splitlines()\n",
    "# print(lines)\n",
    "total = 0\n",
    "for line in lines:\n",
    "    if line.find(\"visitorcnt id\") != -1:\n",
    "        print(line)\n",
    "        result = line.find(\"cnt=\")\n",
    "        print (line[result+4])\n",
    "# view = tree.xpath('//*[@class=\"collapsible\"]/div[1]/div[2]/div[1]/span/span[2]/span[2]/text()')\n",
    "\n",
    "# print(view)\n",
    "    "
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
