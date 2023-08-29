from cards import CARD
from stations import STATION

def card_manager(card_id, amount_added, card_db):
    if card_id in card_db:
        card_db[card_id].balance += int(amount_added)   
    else:
        card_db[card_id] = CARD(card_id, int(amount_added))
    return card_db

def get_trip_summary(card_info,age_grp):
        total_fare,discount = card_info.get_trip_fare(age_grp)
        total_fare = card_info.set_wallet_balance(total_fare)
        return total_fare,discount,card_info

def input_manager(lines):
    ##Initialize stations
    stations_db = {'CENTRAL':STATION('CENTRAL'),'AIRPORT':STATION('AIRPORT')}
    card_db = {}
    for line in lines:
        ip_line = list(line.strip().split(" "))
        if ip_line[0]=='BALANCE':
            card_db = card_manager(ip_line[1], ip_line[2], card_db)

        elif ip_line[0]=='CHECK_IN':
            if ip_line[1] not in card_db:
                raise Exception("User not found")
            total_fare, discount, card_db[ip_line[1]] = get_trip_summary(card_db[ip_line[1]],ip_line[2])
            stations_db[ip_line[3]].put_traveller_entry(ip_line[2],total_fare,discount)

        elif ip_line[0]=='PRINT_SUMMARY':
            for station in stations_db:
                stations_db[station].get_station_summary()