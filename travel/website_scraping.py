expedia_domestic = 'https://www.expedia.com/Flights-Search?trip=roundtrip&leg1=from%3A{d city}%2C%20United%20States%20of%20America%20{d airport code}%2Cto%3A{r city %20 between cities}%2C%20{r state ab}%20(-All%20Airports)%2Cdeparture%3A{d month}%2F{d day}%2F{d year}TANYT&leg2=from%3A{r city %20 betwen}%2C%20{r state ab}%20(-All%20Airports)%2Cto%3A{d city}%2C%20United%20States%20of%20America%20{airport code}%2Cdeparture%3A{r month}%2F{r day}%2F{r year}TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com'

expedia_intl ='https://www.expedia.com/Flights-Search?flight-type=on&starDate={d month}%2F{d day}%2F{d year}&endDate={r month}%2F{r day}%2F{r year}&mode=search&trip=roundtrip&leg1=from%3A{d city}%2C+{d state}+%28{airport code- airport name with + between}%29%2Cto%3A{r city}%2C+{r country}+%28TUN-%29%2Cdeparture%3A03%2F01%2F2020TANYT&leg2=from%3A{r city}%2C+{r country}%29%2Cto%3A{d city}%2C+{d state ab}+%28{{airport ab-airport name with + between}}%29%2Cdeparture%3A{r month}%2F{r day}%2F{r year}TANYT&passengers=children%3A0%2Cadults%3A1%2Cseniors%3A0%2Cinfantinlap%3AY'
#expedia xpath- price = //span[@class='full-bold no-wrap' and @data-test-id='listing-price-dollars']
#departure time = //span[@data-test-id='departure-time'] arrival time= same as departue but with arrival other than departure


priceline = 'https://www.priceline.com/m/fly/search/{origin airport code}-{dest airport code}-{date :yeardaymonth}/{airport return }-{airport return}-{yeardaymonth}/?cabin-class=ECO&num-adults=1&search-type=1111'
#priceline xpathprice = //span[@data-test='rounded-dollars'] times =
'https://www.priceline.com/m/fly/search/NYC-MCO-20190725/MCO-NYC-20190730/?cabin-class=ECO&num-adults=1&search-type=1111'

momondo = 'https://www.momondo.com/flight-search/{airport code origin}-{airport code origin}/{date year-month-day}/{return date}?sort=price_a'
#momondo xpathprice = //span[@class='price-text']

travelocity = 'https://www.travelocity.com/Flights-Search?trip=roundtrip&leg1=from%3A{orgin city}%2C%20{state ab}%2C%20United%20States%20(airport ab)%2Cto%3A{city destination}%2C%20{state ab}%2C%20United%20States%20{(airport ab)}%2Cdeparture%3A{month }%2F{date}%2F{year]TANYT&leg2=from%3A[city name]%2C%20[state ab]%2C%20United%20States%20[(airport ab)]%2Cto%3A[city return ]%2C%20[state ab]%2C%20United%20States%20[(airport id)]%2Cdeparture%3A07%2F29%2F2019TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=www.travelocity.com'
#same as expedia

orbitz = 'https://www.orbitz.com/Flights-Search?flight-type=on&starDate={month}%2F{day}%2F{year}&endDate={month}%2F{day}%2F{year}&_xpid=11905%7C1&mode=search&trip=roundtrip&leg1=from%3A{city}%2C+{state ab}+%28[airport ab CVG-All+Airports]%29%2Cto%3A[des city]%2C+[city]%2Cdeparture%3A[month]%2F[day]%2F[year]TANYT&leg2=from%3A[city]%2C+[city]%2Cto%3A[city]%2C+[state ab]+%28[airport ab CVG-All+Airports]%29%2Cdeparture%3A[month]%2F[day]%2F[year]TANYT&passengers=children%3A0%2Cadults%3A1%2Cseniors%3A0%2Cinfantinlap%3AY'
#same as expedia

hotwire = 'https://vacation.hotwire.com/Flights-Search?tmid=30074710375&trip=RoundTrip&leg1=from:{airport code},to:{airport code},departure:{date with dash}TANYT&leg2=from:{returning airport code},to:{airport code},departure:{date with dash /}TANYT&passengers=children:0,adults:1,seniors:0,infantinlap:Y&options=sortby:price&mode=search&paandi=true'
#same as expedia

seatguru = 'https://www.seatguru.com/flights?from={city}%2C+{state}+-+city%2FNorthern+Kentucky+Airport+%28{airport code}%29&from_loc=&to={city}%2C+{state ab}+-+All+Airports+%28NYC%29&to_loc=&date={month}%2F{day}%2F{year}&fcf_departing={month}%2F{day}%2F{year}&date={month}%2F{day}%2F{year}+-+{month}%2F{day}%2F{year}&fcf_rt_departing=08%2F07%2F2019&fcf_rt_returning=08%2F14%2F2019&radio=on&airport0=CVG&airport1=NYC&oneway=&nonstop=no&travelers=1&cos=0&pax0=a&pax1=&pax2=&pax3=&pax4=&pax5=&infants='
#seatguru xpathprice = //span[@class="flights-search-results-itinerary-card-components-Title__price--xfl94"]
#seatguru times xpath = //div[@class='flights-search-results-itinerary-card-components-OneWayInfo__odTime--mp9Dl']

cheapoair = 'https://www.cheapoair.com/fpnext/Air/Listing/s/2/su/301e41b1-b541-4127-8af2-0ebb51728792'
#cheapoair price xpath = //span[@class='currency'] depart time = //span[@class="depart_time"] arrival time = arival_time


kayak = 'https://www.kayak.com/flights/{airport code to-from}/{date going -}/{date returning -}?sort=bestflight_a'
#kayak xpath price = //span[@class='price option-text']
#dates left = //span[@class="depart-time base-time"]/ampm = //span[@class="time-meridiem meridiem"] arrival =class="arrival-time base-time"



# google_flights = 'https://www.google.com/flights?hl=en#flt=/m/01snm./m/02_286.{year-month-day}*/m/02_286./m/01snm.{return year-month-day};c:USD;e:1;sd:1;t:f'
#google flights prices 2: //div[@class="flt-subhead1 gws-flights-results__price gws-flights-results__cheapest-price"] / //div[@class="flt-subhead1 gws-flights-results__price"]
#google times: //div[@class="gws-flights-results__times flt-subhead1"]

# https://www.google.com/flights?hl=en#flt=/m/01snm./m/02_286.03-01-2029*/m/02_286./m/01snm.{return year-month-day};c:USD;e:1;sd:1;t:f

skyscanner = 'https://www.skyscanner.com/transport/flights/{airport code}a/{airportcode}a/{date 190722}/{return date}/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home#results'
#skyscanner price = //a[@class="CTASection__price-2bc7h price"]
#skyscanner times = //span[@class="LegInfo__times-Qn_ji"]
