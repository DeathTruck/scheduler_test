import pandas as pd
import numpy as np
import comments_scrape
import prescan
import time
import datetime
import os

movie_list= pd.read_csv("/Users/nikolaushbuenning/CSVs/NRG_movielist_week2-21.csv")
ids = list(movie_list.entity_id)
for i in ids:
    print(i)
    dumtime = datetime.datetime.now()
    time_stamp = str(dumtime.year) +"-"+ str(dumtime.month)+"-"+ str(dumtime.day)+"-"+str(dumtime.hour)
    prescan.main_scrape(str(i))
    filein = '%s_facebook_statuses.csv' % i
    fileout = '%s_facebook_statuses_%s.csv' % (i, time_stamp)
    command = "cp "+filein+" "+fileout
    print(command)
    os.system(command)
    # comments_scrape.main_scrape_comments(str(i))
