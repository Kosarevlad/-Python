def personal_info(**kwargs):
    return kwargs
x = (personal_info(name=input("Name"), surname=input("Surname"), berthday=input("Berthday"), city=input("Sity"), email=input("email"), phone_number=input("Phone_number")))
print(x.values())

