from selenium import webdriver
from collections import Counter

s = "https://www.adventofcode.com/2021/leaderboard/day/"
driver = webdriver.Firefox()

overall = Counter()
for i in range(1,26):
    url = s + str(i)
    driver.get(url)
    leaderboard = driver.find_elements_by_class_name("leaderboard-entry")
    for l in range(len(leaderboard)):
        overall[leaderboard[l].text[23:]] += 100 - l if l < 100 else 200 - l
    
