#hltv
from bs4 import BeautifulSoup
import urllib2
import json
import requests


team = raw_input("Enter Team Name ---> ")
req = urllib2.Request("http://esportlivescore.com/g_csgo.html")
req.add_header('User-Agent', 'Mozilla/5.0')
resp = urllib2.urlopen(req)
hltv = resp.read()
soup = BeautifulSoup(hltv, 'html.parser')
match = soup.find('img', title=team)
i = 0
while i<5:
    match = match.parent
    i+=1
team1 = match.find('tr', class_='event-home-team').find('td', class_='participant-name   init-click-done').a.text
team2 = match.find('tr', class_='event-away-team').find('td', class_='participant-name   init-click-done').a.text
map1score1 = match.find('span', class_='home-set1 event-score-set1')
map1score2 = match.find('span', class_='away-set1 event-score-set1')
map2score1 = match.find('span', class_='home-set2 event-score-set2')
map2score2 = match.find('span', class_='away-set2 event-score-set2')
map3score1 = match.find('span', class_='home-set3 event-score-set3')
map3score2 = match.find('span', class_='away-set3 event-score-set3')
text = []
text.append(team1+" vs. "+team2+" "+match.find('span', style='font-size:9px;').text)
if len(map1score1.text)>0:
    text.append("Map 1: "+map1score1.text+" - "+map1score2.text)
if len(map2score1.text)>0:
    text.append("Map 2: "+map2score1.text+" - "+map2score2.text)
if len(map3score1.text)>0:
    text.append("Map 3: "+map3score1.text+" - "+map3score2.text)


slack_integration_url = "https://hooks.slack.com/services/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"
requests.post(slack_integration_url, json.dumps({ 'text': '\n'.join(text) }))
