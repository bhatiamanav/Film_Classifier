import random
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

imdbdata = pd.read_csv('IMDB-Movie-Data.csv')

imdbdata = imdbdata.rename(columns = {'Revenue (Millions)':'Revenue_Millions'})
imdbdata = imdbdata.rename(columns = {'Runtime (Minutes)':'Runtime_Minutes'})

#imdbdata.Director.value_counts()[:10].plot.pie(autopct='%1.1f%%',figsize=(20,20))
#plt.title('Top 10 Movie Directors')
#plt.show()

#imdbdata.Actors.value_counts()[:10].plot.pie(autopct='%1.1f%%',figsize=(20,20))
#plt.title('Top 10 Movie Actors')
#plt.show()

#sns.stripplot(x="Year",y="Rating", data=imdbdata,jitter=True)
#plt.title('Rating Based on Year')
#plt.show()

#sns.swarmplot(x="Year", y="Votes", data=imdbdata)
#plt.title('Votes Based on Year')
#plt.show()

#sns.stripplot(x="Year", y="Revenue_Millions", data=imdbdata, jitter=True)
#plt.title('Revenue Based on Year')
#plt.show()

#sns.swarmplot(x="Year", y="Metascore", data=imdbdata)
#plt.title('Metascore Based on Year')
#plt.show()

imdbdata["Rating"].value_counts()
 
Sortedrating= imdbdata.sort_values(['Rating'], ascending=False)

lowratedmovies= imdbdata.query('(Rating > 0.0) & (Rating < 3.0)')

sns.jointplot(x="Rating", y="Metascore", data=lowratedmovies)
plt.title('(Movies with Low Rating , METASCORE')
plt.show()

sns.jointplot(x="Rating", y="Votes", data=lowratedmovies)
plt.title('(Movies with Low Rating , VOTES')
plt.show()

sns.jointplot(x="Rating", y="Revenue_Millions", data=lowratedmovies)
plt.title('(Movies with Low Rating , REVENUE')
plt.show()

mediumratedmovies= imdbdata.query('(Rating > 3.0) & (Rating < 7.0)')

sns.jointplot(x="Rating", y="Metascore", data=mediumratedmovies)
plt.title('(Movies with Medium Rating , METASCORE')
plt.show()

sns.jointplot(x="Rating", y="Votes", data=mediumratedmovies)
plt.title('(Movies with Medium Rating , VOTES')
plt.show()

sns.jointplot(x="Rating", y="Revenue_Millions", data=mediumratedmovies)
plt.title('(Movies with Medium Rating , REVENUE')
plt.show()

highratedmovies= imdbdata.query('(Rating > 7.0) & (Rating < 10.0)')

sns.jointplot(x="Rating", y="Metascore", data=highratedmovies)
plt.title('(Movies with High Rating , METASCORE')
plt.show()

sns.jointplot(x="Rating", y="Votes", data=highratedmovies)
plt.title('(Movies with High Rating,VOTES')
plt.show()

sns.jointplot(x="Rating", y="Revenue_Millions", data=highratedmovies)
plt.title('(Movies with High Rating ,REVENUE')
plt.show()

metascore=imdbdata.Metascore
sns.boxplot(metascore)
plt.show()
