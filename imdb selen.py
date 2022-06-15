import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



df=pd.read_csv(r'C:\Users\karee\Desktop\python projects\imdb\IMDB (1).csv')
# Selenium------------------------------------------------------------------------------------------------------------------------------------------------------
path="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get('https://www.imdb.com/chart/top')

first=driver.find_element(By.CLASS_NAME,'lister-list')# main page

links=[]
titles=driver.find_elements(By.CLASS_NAME,'titleColumn') #the list for the movies
for title in titles:#for every list i want you to find the element that has the movie's link
    links.append(title.find_element(By.CSS_SELECTOR,'a').get_attribute('href'))# the link for each movie
Director=[]
Star=[]
Writers=[]
for link in links: #for each movie enter, the link then get the director, writers and the first Star
    driver.get(link)
    Writer=[]
    
    
    # Director


    director=driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[1]/div/ul/li/a').text
    Director.append(director)


    # WRITER
    FIRST=driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[2]/div/ul')
    #the first step contains the list of writers
    writers=FIRST.find_elements(By.TAG_NAME,'a') #this is inside the list

    for x in writers: #for each writer you find inside the list add his/her name to the first list
        Writer.append(x.text)
    Writers.append(','.join(Writer)) #because their can be several writers for the same movie, i did two lists, one for the writers
    # of each movie and one for entire dataset. 
    # now each movie will have:    Movie -->  writer: name,name,name
        

#  STARS
    FIRST=driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[3]/div/ul')
    SECOND=FIRST.find_element(By.CLASS_NAME,'ipc-inline-list__item')
    stars=SECOND.find_elements(By.TAG_NAME,'a')
    for star in stars:
        Star.append(star.text)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PANDAS-------------------------------------------------------------------------------------------------------------------------------

# adding columns
df['Writer']=Writers
df['Director']=Director
df['Stars']=Star
df['More info']=links

# saving to the dataset
# df.to_csv('IMDB.csv',index= False)

print(df)
# # ----------------------------------------------------------------------------------------------------------------------------------------------------------
# print('Done') #KAREEM ABOUELSEOUD.

