names = ["Bauka" , "Bolat", "Akame", "Sakurajima"]
with open('names.txt', "w") as myfile:
        for c in names:
                myfile.write("%s\n" % c)

content = open('names.txt')
print(content.read())
