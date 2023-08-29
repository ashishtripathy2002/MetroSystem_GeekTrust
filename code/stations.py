class STATION:
    def __init__(self,station):
        self.station = station
        self.passenger_age_cnt = {'ADULT': 0, 'SENIOR_CITIZEN': 0, 'KID': 0}
        self.total_sale = 0.0
        self.total_discount = 0.0
    
    def get_station_summary(self):
        print(f"TOTAL_COLLECTION {self.station} {int(self.total_sale)} {int(self.total_discount)}")
        print("PASSENGER_TYPE_SUMMARY")
        sorted_passenger_counts = sorted(self.passenger_age_cnt.items(), key=lambda x: (-x[1], x[0]))
        for passenger_type, count in sorted_passenger_counts:
            if count>0:
                print(f"{passenger_type} {count}")

    def put_traveller_entry(self,passenger_age_grp,fare,discount):
        self.passenger_age_cnt[passenger_age_grp] += 1
        self.total_sale += fare
        self.total_discount +=discount