import requests
import re
import json

url = 'https://www.dmxq.fun/vodplay/15500-1-3.html' # 毒枭第一季
# url = input('Please input movie url: ')
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
r = requests.get(url=url, headers=headers)
aaaa = re.findall('var player_aaaa=(.*?)</script>', r.text)[0]
json_aaaa = json.loads(aaaa)
mov_title = json_aaaa['vod_data']['vod_name']
aaaa_script = '<script type="text/javascript">var player_aaaa=' + aaaa + '</script>'
ep_title = re.findall('var ep_title = "(.*?)";', r.text)[0]
title = re.findall('document.title = (.*?);', r.text)[0]
var_ep_title = f'var ep_title = "{ep_title}";'
doc_title = f'document.title ={title};'.replace('免费在线观看-大米星球','')

with open('template.text', 'r') as temp:
    template = temp.read()

    template= template.replace('replace_script', aaaa_script)
    template = template.replace('replace_ep_title', var_ep_title)
    template = template.replace('replace_document_title', doc_title)
    # print(template)

with open(f'{ep_title}.html','w',encoding='utf-8') as f:
    f.write(template)