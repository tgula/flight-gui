import sqlite3
import pickle
from csv import writer

trav = sqlite3.connect('travel_database.db')
t = trav.cursor()

def create_table():
    t.execute('''CREATE TABLE IF NOT EXISTS travel (
    city TEXT, state TEXT, abb TEXT, dest_city TEXT, dest_state TEXT,
    airport TEXT, airport_ab TEXT, miles TEXT)''')
# ---------open pickled data and create variables -------
with open('ohio_dayton.pkl','rb') as pickle_file:
    dayton = pickle.load(pickle_file)
with open('ohio_cincinnati.pkl','rb') as pickle_file:
    cincinnati = pickle.load(pickle_file)
with open('ohio_columbus.pkl','rb') as pickle_file:
    columbus = pickle.load(pickle_file)
with open('ohio_cleveland.pkl','rb') as pickle_file:
    cleveland = pickle.load(pickle_file)
with open('ohio_akron.pkl','rb') as pickle_file:
    akron = pickle.load(pickle_file)
with open('ohio_toledo.pkl','rb') as pickle_file:
    toledo = pickle.load(pickle_file)

home_city = [[['Dayton','Ohio','OH','OH','Dayton','James M Cox Dayton International', 'DAY'],0],[['Cleveland', 'Ohio','OH', 'OH', 'Cleveland', 'Cleveland-Hopkins International', 'CLE'], 0],
[['Akron', 'Ohio','OH', 'OH', 'Akron','Akron-Canton Regional', 'CAK'], 0],[['Toledo', 'Ohio','OH', 'OH', 'Toledo', 'Toledo Express', 'TOL'], 0],
[['Columbus', 'Ohio', 'OH', 'OH', 'Columbus','John Glenn Columbus International', 'CMH'], 0],[['Columbus', 'Ohio','OH', 'OH', 'Columbus','Rickenbacker International', 'LCK'], 0]]
city_list = [dayton,cincinnati,columbus,cleveland,akron,toledo,home_city]

#------------------- lists of data-----------------
def data_entry(data_list):
        for item in data_list:
        #Home city, home state, state ab,airport state destination, city, airport name, abbreviation, miles
            for data in item: #loop through list and
                print (data)
                if len(data[0])==7:
                    t.execute('''INSERT INTO travel (
                    city, state, abb, dest_city, dest_state ,
                    airport, airport_ab, miles) VALUES (?,?,?,?,?,?,?,?)''',
                    (data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],
                data[0][6],data[1]))

                else:
                    pass
        trav.commit()
        print("Record inserted successfully into SqliteDb_developers table ", t.rowcount)
        trav.close()



if __name__=='__main__':
    create_table()
    data_entry(city_list)
    print ('DATA HAS BEEN ENTERED')
