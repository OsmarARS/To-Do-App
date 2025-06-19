contents = ["Osmar", "Aldair", "Ramirez"]

filenames = ["firstname.txt", "secondname.txt", "lastname.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", "w")
    file.write(content)