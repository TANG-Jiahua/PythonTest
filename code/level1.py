import datetime
import json

with open("../backend/level1/data/input.json") as file:
    load = json.load(file)
  #  print(load)
cars = load['cars']
rents = load['rentals']

rentals = {}
rentals_list = []
rental_id = 0

for rent in rents:
    rental_id += 1
    start_date = datetime.datetime.strptime(rent['start_date'], "%Y-%m-%d")
    end_date = datetime.datetime.strptime(rent['end_date'], "%Y-%m-%d")
    days = end_date - start_date
    car = cars[rent['car_id'] - 1]
    price_day = car['price_per_day'] * (days.days + 1)
    # print(price_day)
    price_km = car['price_per_km'] * rent['distance']
    price = price_day + price_km
    rentals_list.append({'id': rental_id, 'price': price})

rentals['rentals'] = rentals_list

json_str = json.dumps(rentals)
print(json_str)

with open('../outputs/level1_output.json', 'w') as file:
    file.write(json_str)
