phone_number = "027778888"
phone_number = phone_number.replace(phone_number[0:len(phone_number)-4], '*' * (len(phone_number)-4))
print(phone_number)


print("*" * (len(phone_number)-4) + phone_number[-4:])