import pandas as pd
import numpy as np

def read_1980_Movies_Rating():
  '''
  No input
  Read CSV database_1980_Rating.csv from Github
  Return a DataFrame with 'genres' in list type
  '''
  #read the CSV file
  df_movies=pd.read_csv('https://raw.githubusercontent.com/AudreyMuller/Recommandation_Films_1980_s/Main/00_CSV/database_1980_Rating.csv', sep=';')
  
  #dropt the first column created woth 'to_CSV'
  df_movies.drop(columns='Unnamed: 0',inplace=True)
  #convert 'genres' en list  --> .split(',')
  df_movies['genres'] = df_movies['genres'].apply(lambda x: eval(x.strip()))

  #set 'tconst' as Index
  df_movies.set_index('tconst',inplace=True)
  return df_movies