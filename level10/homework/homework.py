# 2) კომენტარის სახით დაწერეთ თუ რა დანიშნულება აქვს type() ფუნქციას და რატომაა მისი გამოყენება მოხერხებული.

# type ფუნქცია გვეხმარება გავიგოთ თუ რომელ data type-ს ეკუთხვნის ესა თუ ის ინფორმაცია

# 3) ჩამოწერეთ ყველა ის ფუნქცია რომელიც “Data Conversion”-ს მოიცავს. გატესტეთ თითოეული ყველა ნასწავლ მონაცემთა ტიპზე.

# int() – გარდაქმნის მთელ რიცხვად (Integer)

# float() – გარდაქმნის ათწილადად (Float)

# str() – გარდაქმნის სტრინგად (String)

# bool() - გარდაქმნის Boolean ტიპად (True/False)

# 4) ცვლადებში შეინახეთ თქვენი სახელი,  გვარი და ასაკი (Integer) . ტერმინალში გამოიტანეთ წინადადება - რომელსაც კონკატინაციის შედეგად მიიღებთ. ვიცით რომ String-სა და Integer-ს შორის მათემატიკურ ოპერაციას ვერ შევასრულებთ, შესაბამისად დაწერეთ ისეთი კოდი, რომ Error-ების გარეშე გაეშვას ტერმინალში.
name = 'Tato'
surname = 'Afanasieva'
age = 15
print('მე ვარ ' + name + ' ' + surname + ' და მე ვარ ' + str(age) + ' წლის')

# 5) მომხმარებელს შემოატანინეთ 5 რიცხვი. დაწერეთ პროგრამა, რომელიც გამოთვლის და დაბეჭდავს ამ რიცხვების საშუალო არითმეტიკულს. 

#  (საშუალო არითმეტიკული - რიცხვთა ჯამის განაყოფი რიცხვების რაოდენობაზე)

num1 = int(input('enter random number: '))
num2 = int(input('enter random number: '))
num3 = int(input('enter random number: '))
num4 = int(input('enter random number: '))
num5 = int(input('enter random number: '))

print((num1 + num2 + num3 + num4 + num5) / 5)


# 6) მომხმარებელს შემოატანინეთ ტემპერატურა ცელსიუსში. დაწერეთ პროგრამა, რომელიც მომხმარებლის მიერ შემოტანილ ტემპერატურას გადაიყვანს ფარენგეიტში და დაბეჭდეთ საბოლოო შედეგი. (მოიძიეთ ფორმულა ინტერნეტში)
temp = int(input("Enter temperature: "))
print((temp * 9/5) + 32)

# 7) მეხუთე დავალების მსგავსად, შემოატანინეთ მომხმარებელს ტემპერატურა, თუმცა ამჯერად - ფარენგეიტში. შემდეგ კი დაწერეთ პროგრამა, რომელიც შემოტანილ ტემპერატურას ცელსიუსში გადაიყვანს და საბოლოოდ დაბეჭდეთ შედეგი.
temp1 = int(input("Enter temperature: "))
print((temp1 - 32) * 5/9)