import tkinter as tk
import sqlite3
from bs4 import BeautifulSoup
import random
from selenium import webdriver
import time
import webbrowser


class Travel:
    #import database that includes city,state,airport city/state abbreviation,miles away from home city
    trav = sqlite3.connect('travel_database.db')
    t= trav.cursor()
    all_database= t.execute("SELECT * FROM travel")
    my_rows = all_database.fetchall()

    def __init__(self, parent):
        self.parent = parent
        self.title = parent.title('Travel Site')
        self.state = list({ci[2] for ci in Travel.my_rows}) #states in database
        self.city = list({state[0] for state in self.my_rows if state[2] in self.state}) #city in database only if in state selected.

        #city variable
        self.city_variable = tk.StringVar(self.parent)
        self.city_variable.set('')
        self.city_variable.trace('w', self.update_option_menu)

        #state dropdown
        self.state_label = tk.Label(self.parent,text='State:').grid(row=1,column=0)
        self.state_variable = tk.StringVar(self.parent)
        self.state_variable.set('')
        self.state_dropdown = tk.OptionMenu(self.parent, self.state_variable, *self.state)
        self.state_dropdown.grid(row=1,column=1)

        #city dropdown
        self.city_label = tk.Label(self.parent,text='City:').grid(row=2,column=0)
        self.city_dropdown = tk.OptionMenu(self.parent, self.city_variable, *self.city)
        self.city_dropdown.grid(row=2,column=1)



        #destination city/state begins
        self.destination_city= tk.StringVar(self.parent)
        self.destination_state = tk.StringVar(self.parent)
        self.dest_city = tk.Entry(root,textvariable=self.destination_city).grid(row=3,column=1,padx=17,pady=19)
        self.dest_state = tk.Entry(root,textvariable=self.destination_state).grid(row=4,column=1,padx=17,pady=19)
        dest_city = tk.Label(root, text='Destination City:').grid(row=3,column=0)
        dest_state = tk.Label(root, text='Destination State (abbreviation):').grid(row=4,column=0)

        #date depart
        self.date = tk.StringVar(self.parent)
        self.date_entry = tk.Entry(root,textvariable=self.date).grid(row=5,column=1,padx=17,pady=19)
        self.date_label= tk.Label(root,text='Enter date in following format MM/DD/YYYY:').grid(row=5,column=0)

        #date return
        self.date_return = tk.StringVar(self.parent)
        self.date_entry_return = tk.Entry(root,textvariable=self.date_return).grid(row=6,column=1,padx=17,pady=19)
        self.date_label_return = tk.Label(root,text='Enter return date in following format MM/DD/YYYY:').grid(row=6,column=0)

        #miles
        self.miles = tk.StringVar(parent)
        self.miles_entry = tk.Entry(root,textvariable=self.miles).grid(row=7,column=1,padx=17,pady=19)
        self.miles_label = tk.Label(root,text='Miles From Home City:').grid(row=7,column=0)

        #submit button that gets all variables entered
        self.submit = tk.Button(root,text='SUBMIT',command=self.gather_info).grid(row=8,column=0,padx=17,pady=19)

    #update city dropdown depending on state selected
    def update_option_menu(self,*args):
        menu = self.city_dropdown["menu"]
        menu.delete(0, "end")
        for string in self.city:
            menu.add_command(label=string,
                             command=lambda value=string: self.city_variable.set(value))

    #link to flight selected on flight info page
    def website_link(u):
        webbrowser.open_new(u)

    #submit button function that gathers information and scrapes website and displays on separate page
    def gather_info(self):

        city=self.city_variable.get()
        state=self.state_variable.get()
        dest_c = self.destination_city.get()
        dest_s = self.destination_state.get()
        date = self.date.get()
        date_return = self.date_return.get()
        miles = self.miles.get()
        info = [city,state,dest_c,dest_s,date,date_return,miles] #put all entry variables into list
        #loops through database and filters all cities according to entries given.
        airport_list = list({air for air in Travel.my_rows  if air[0].lower() == info[0].lower() and air[2].lower()==info[1].lower() and int(air[-1]) <= int(info[-1])})
        #get both dates and if its intl or domestic and destination city/state
        date = date.split('/')
        date_return = date_return.split('/')
        travel_info_list = []
        driver = webdriver.Chrome()
        #loop through airport lists that have passed conditions in entry and search website.
        for airport in airport_list:
            url ='https://www.expedia.com/Flights-Search?flight-type=on&starDate={0}%2F{1}%2F{2}&endDate={3}%2F{4}%2F{5}&mode=search&trip=roundtrip&leg1=from%3A{6}%2C+{7}+%28{8}%29%2Cto%3A{9}%2C+{10}+%28%29%2Cdeparture%3A{11}%2F{12}%2F{13}TANYT&leg2=from%3A{14}%2C+{15}%29%2Cto%3A{16}%2C+{17}+%28{18}%29%2Cdeparture%3A{19}%2F{20}%2F{21}TANYT&passengers=children%3A0%2Cadults%3A1%2Cseniors%3A0%2Cinfantinlap%3AY'.format(date[0],date[1],date[2],date_return[0],date_return[1],date_return[2],airport[4].replace(' ','%20'),airport[4],airport[-2],info[2].replace(' ','%20'),info[3].replace(' ','%20'),date[0],date[1],date[2],info[2].replace('','%20'),info[3].replace(' ','%20'),airport[4].replace(' ','%20'),airport[3].replace(' ','%20'),airport[-2],date_return[0],date_return[1],date_return[2])
            driver.get(url)
            time_list = random.randint(7,12) #delay for dynamic javascript
            time.sleep(time_list)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            expedia_price = soup.find_all('span',class_="full-bold") #scrape price
            for price in expedia_price:
                price=price.text
                travel_info_list.append([price,url,airport[3],airport[4],info[2],
                info[3],info[4],info[5]])# list returns the price, the url, the home state,home city,destination state, destination city, and the dates

        lowest_price = [p[0] for p in travel_info_list] #get the price as a string
        lowest_price_dig = sorted([int(p[1:].replace(',','')) for p in lowest_price])[:5] #get the top 5 prices
        lowest_price_info = [info for info in travel_info_list if int(info[0][1:].replace(',','')) in lowest_price_dig] #for prices in thousands
        top=tk.Toplevel()
        top.title('Cheapest Flights')
        trip_date = tk.Label(top,text='DATE').grid(row=0,column=0,padx=15,pady=15)
        trip_destinations = tk.Label(top,text='TRIP').grid(row=0,column=1,padx=15,pady=15)
        trip_price = tk.Label(top,text='PRICE').grid(row=0,column=2,padx=15,pady=15)
        trip_link = tk.Label(top,text='LINK').grid(row=0,column=3,padx=15,pady=15)
        r=1
        for x in lowest_price_info:
            for y in range(len(x)-1):
                #post scraped info into second page.
                date_given = '{}-{}'.format(x[-2],x[-1])
                cities = '{},{}-{},{}'.format(x[3].title(),x[2].upper(),x[4].title(),x[5].upper())

                date_scrape= tk.Label(top,text=date_given).grid(row=r,column=0,padx=15,pady=15)
                dest= tk.Label(top,text=cities).grid(row=r,column=1,padx=15,pady=15)
                price_scrape= tk.Label(top,text=x[0]).grid(row=r,column=2,padx=15,pady=15)
                link_scrape = tk.Button(top, text="LINK", fg="blue", command=lambda:Travel.website_link(x[1].replace(' ',''))).grid(row=r,column=3,padx=15,pady=15)
                r+=1




root = tk.Tk()
Travel(root)
root.mainloop()
