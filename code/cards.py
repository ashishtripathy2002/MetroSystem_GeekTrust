class CARD:
    def __init__(self, card_id, balance):
        self.card_id = card_id
        self.balance = balance
        self.single_trip_status = False
    
    def get_trip_fare(self,age_grp):
        fare_tab = {'ADULT': 200.0, 'SENIOR_CITIZEN': 100.0, 'KID': 50.0}
        discount = total_fare = 0.0
        total_fare = 0.5 *fare_tab[age_grp] if self.single_trip_status else fare_tab[age_grp]
        discount = total_fare if self.single_trip_status else 0.0
        return total_fare,discount
    
    def set_wallet_balance(self,total_fare):
        tax = 0.02
        new_balance = self.balance - total_fare
        ##Update fare incase of recharge
        if new_balance<0:
            total_fare += -tax * new_balance 
            new_balance = 0.0
        self.balance =new_balance
        self.single_trip_status = not self.single_trip_status
        return total_fare