import requests
import sys
import re
from lxml import html

debug = True
error_count = 0
proxy_count = 0

def dg(line):
    if debug==True:
        print "[Debug]" + line


def Source_1():
    url_list = {'https://free-proxy-list.net/anonymous-proxy.html',
                'https://free-proxy-list.net/uk-proxy.html',
                'https://free-proxy-list.net/',
                'https://www.us-proxy.org/'}
    for url in url_list:
        is_online = False
        dg('Testing URL')
        try:
            #url = "https://free-proxy-list.net/anonymous-proxy.html"
            r = requests.get(url)
            is_online = True
            dg('URL is online')
        except:
            dg('URL not found')

        dg('Writting to file')
        if is_online == True:
            for td in range(1,80):
                proxies = open('proxies.txt', 'a+')
                try:
                    tree = html.fromstring(r.content)
                    ip = tree.xpath('//*[@id="proxylisttable"]/tbody/tr[' + str(td) + ']/td[1]/text()')
                    port = tree.xpath('//*[@id="proxylisttable"]/tbody/tr[' + str(td) + ']/td[2]/text()')
                    entry = ip[0] + ':' + port[0] + '\n'
                    proxies.write(entry)
                    proxies.close
                except:
                    dg('Current XPath not found')
                    proxies.close


def main():
    dg('Starting scraper')
    #dg('Scraping from https://free-proxy-list.net/anonymous-proxy.html')
    Source_1()
    

if __name__=="__main__":
    main()
