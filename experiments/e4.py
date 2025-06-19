waiting_list = ["sen", "ben", "john"]
waiting_list.sort(reverse=True)

for index, pacient in enumerate(waiting_list):
    row = f"{index + 1}.{pacient.capitalize()}"
    print(row)