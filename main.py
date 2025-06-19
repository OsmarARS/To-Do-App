filenames = ["1.doc", "2.report", "1.presentation"]

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
print(filenames)