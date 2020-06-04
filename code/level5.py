import datetime
import json

with open("../backend/level5/data/input.json") as file:
    load = json.load(file)
  #  print(load)
cars = load['cars']
rents = load['rentals']
options = load['options']

rentals = {}
rentals_list = []
rental_id = 0

def getPrice_Day(price,days):
    prices = price 
    if( days > 1 ):
        if( days >4 ):
            if( days > 10 ):  #more than 10 days
               prices += ( price * 2.7 + price * 4.2 + price * ( days - 10) * 0.5) 
            else:  #more than 4 days but less than 10 days
                prices += ( price * 2.7 + price * ( days - 4 ) * 0.7)
        else:   #more than 1 day but less than 4 days
            prices += price * (days-1) *0.9
    return int(prices)

for rent in rents:
    option = []
    actions = []
    rental_id += 1
    
    start_date = datetime.datetime.strptime(rent['start_date'], "%Y-%m-%d")
    end_date = datetime.datetime.strptime(rent['end_date'], "%Y-%m-%d")
    days =int( (end_date - start_date ).days)+1
    
    car = cars[rent['car_id'] - 1]
    
    price_day = getPrice_Day(car['price_per_day'],days)
    price_km = car['price_per_km'] * rent['distance']
    price = price_day + price_km

    driver = price
    owner = int(price * 0.7)
    insurance = int(price * 0.15)
    assitance = int((days)*100)
    drivy = int(price * 0.15 - assitance)
    
    for op in options:
        if(op['rental_id']==rent['id']):
           option.append(op['type'])
           if(op['type']=='gps'):
               driver+=500*days
               owner+=500*days
           elif(op['type']=='baby_seat'):
                driver+=200*days
                owner+=200*days
           else:
               driver+=1000*days
               drivy+=1000*days
               

 #   actions.append([{ 'who':'driver','type':'debit','amount':driver},
  #                 { 'who':'owner','type':'credit','amount':owner},
   #                { 'who':'insurance','type':'credit','amount':insurance},
    #               { 'who':'assitance','type':'credit','amount':assitance},
     #              { 'who':'drivy','type':'credit','amount':drivy}])

    actions.append({ 'who':'driver','type':'debit','amount':driver})
    actions.append({ 'who':'owner','type':'credit','amount':owner})
    actions.append({  'who':'insurance','type':'credit','amount':insurance})
    actions.append({ 'who':'assitance','type':'credit','amount':assitance})
    actions.append({ 'who':'drivy','type':'credit','amount':drivy})
           
    rentals_list.append({'id': rental_id,'options': option,'actions': actions})

rentals['rentals'] = rentals_list

json_str = json.dumps(rentals)
print(json_str)

with open('../outputs/level5_output.json', 'w') as file:
    file.write(json_str)
