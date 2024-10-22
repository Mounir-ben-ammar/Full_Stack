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

    def spend_points (self, amount):
        self.gold_card_points -=  amount

    def display_info (self):

        print(f"first name: {self.first_name} \nLast name: {self.last_name} ")
        print(self.email)
        print(self.age)
        print(self.gold_card_points)
        print(self.rewards_member)


mounir_user = User ("Mounir", "Ben Amma", "mounir@gmail.com", 37)
mounir_user.display_info()
mounir_user.enroll()
mounir_user.spend_points(80)
mounir_user.display_info()


