from bs4 import BeautifulSoup as bs
import requests,csv

html_file= requests.get('https://www.imdb.com/chart/top/')
soup=bs(html_file,'lxml')


file=open('IMDB.csv','w',encoding='utf-8',newline='') #opens a new csv, writing mode, encodes it and doesnt add a line between each row 
writer=csv.writer(file)
writer.writerow(['Rank','Name','Date','Rating']) #HEADERS.

list=soup.find('tbody',class_='lister-list') #it's a checkpoint for me to bring the name and the rating.

movies=list.find_all('tr')
links=[]
print('Loading..............................')
for movie in movies:
    movie_disc=movie.find('td',class_='titleColumn').text.split('\n',4) #contains the rank, name, and date published so i made it a list and each index contains one of these things
    movie_disc1=movie.find('td',class_='titleColumn')#contains the links
    movie_rank=movie_disc[1].replace(' ','').replace('.','') #remove the '.' after each rank and all the spaces
    movie_name=movie_disc[2].replace(' ','',6)#remove the first six spaces from the name as it appears on all the names
    movie_date=movie_disc[3].replace('(','').replace(')','')#remove the brackets from the date
    movie_rating=movie.find('td', class_='ratingColumn imdbRating').text.strip()
    links.append(movie_disc1.a['href'])

    print(f"""Rank: {movie_rank}
    Name:{movie_name}
    Date:{movie_date}
    Rating:{movie_rating}
    """) #output

    writer.writerow([movie_rank ,movie_name ,movie_date ,movie_rating ]) #transfer data to csv

file.close()
# Kareem
