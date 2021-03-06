import datetime
import json

with open("../backend/level3/data/input.json") as file:
    load = json.load(file)
    #print(load)
cars = load['cars']
rents = load['rentals']

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
    rental_id += 1
    start_date = datetime.datetime.strptime(rent['start_date'], "%Y-%m-%d")
    end_date = datetime.datetime.strptime(rent['end_date'], "%Y-%m-%d")
    days = end_date - start_date 
    car = cars[rent['car_id'] - 1]
    price_day = getPrice_Day(car['price_per_day'],days.days+1)
    price_km = car['price_per_km'] * rent['distance']
    price = price_day + price_km
    insurance = int(price * 0.15)
    assitance = int((days.days + 1)*100)
    drivy = int(price * 0.15 - assitance)
    rentals_list.append({'id': rental_id, 'price': price,
                         'commission':{'insurance_fee':insurance,
                        'assistance_fee':assitance,'drivy_fee':drivy}})

rentals['rentals'] = rentals_list

json_str = json.dumps(rentals)
print(json_str)

with open('../outputs/level3_output.json', 'w') as file:
    file.write(json_str)
