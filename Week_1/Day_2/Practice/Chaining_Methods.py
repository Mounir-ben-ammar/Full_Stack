class  User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.rewards_member = False
        self.gold_card_points = 0

    def enroll (self):
        self.gold_card_points = 200
        self.rewards_member = True

        return self
    

    def spend_points (self, amount):
        self.gold_card_points -=  amount

        return self

    def display_info (self):

        print(f"first name: {self.first_name} \nLast name: {self.last_name} ")
        print(self.email)
        print(self.age)
        print(self.gold_card_points)
        print(self.rewards_member)

        return self


mounir_user = User ("Mounir", "Ben Amma", "mounir@gmail.com", 37)
mounir_user.display_info().enroll().spend_point(80).display_infos()


# mounir_user.enroll()
# mounir_user.spend_points(80)
# mounir_user.display_info()


