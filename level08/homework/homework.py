# 2) მომხმარებელს შემოატანინეთ მისი ქალაქის, უბნის, კორპუსის და სართულის შესახებ ინფორმაცია (რომლებიც უნდა შეინახოთ ცალ-ცალკე ცვლადებში). მაგ. city = "Tbilisi", District = "Gldani" და ა.შ. საბოლოოდ print() ბრძანების საშუალებით ტერმინალში გამოიტანეთ მომხმარებლის სრული მისამართი.

city = input("In which city do U live?: ")
District = input("In which district do u live?: ")
Corps = input("In which corps do u live?: ")
floor = input("In which floor do u live?: ")
print(f"მე ვცხოვრობ ქალაქ {city}ში, უბანი: {District}, კორპუსი: {Corps} და სართული {floor}")
# 3) მომხმარებელს შემოატანინეთ ასაკი და f სტრინგის გამოყენებით დაუბეჭდეთ მსგავსი ფორმატის წინადადება: 
# "You are ასაკი years old".
age = int(input("Enter your age: "))
print(f"You are {age} years old")

# 4) შექმენით ორი ცვლადი: Num1 და Num2. ორივე ცვლადში შინახეთ input-ი, სადაც მომხმარებელმა სასურველი რიცხვები უნდა შემოიტანოს. ამ ოპერაციის დასრულების შემდეგ სცადეთ რომ Num1-სა და Num2-ს შორის განახორციელოთ მათემატიკური ოპერაცია და დააკვირდით ტერმინალში შედეგს. ახსენით თქვენი აზრით რატომ მივიღეთ ასეთი შედეგი.
Num1 = int(input("Enter random number: "))
Num2 = int(input("Enter random number: "))
print(Num1 + Num2)
print(Num1 - Num2)
print(Num1 * Num2)
print(Num1 / Num2)
print(Num1 // Num2)
print(Num1 % Num2)
print(Num1 ** Num2)
# მომხმარებელს შემოვატანინეთ ორი რიცხვი და შემდეგ ავტომატურად დავუპრინტეთ მათ შორის განხორციელებული მათემატიკური ოპერაციების შედეგი

# 5) მეოთხე დავალების ანალოგიურად - სცადეთ მომხმარებლის მიერ შემოტანილ ორ რიცხვს შორის შეასრულოთ ყველა მათემატიკური ოპერაცია, რომელიც აქამდე ვისწავლეთ. ამ შემთხვევაშიც დააკვირდით შედეგს და ეცადეთ თქვენი სიტყვებით ახსნათ მიღებული რესულტატი.

Num1 = int(input("Enter random number: "))
Num2 = int(input("Enter random number: "))
print(Num1 + Num2)
print(Num1 - Num2)
print(Num1 * Num2)
print(Num1 / Num2)
print(Num1 // Num2)
print(Num1 % Num2)
print(Num1 ** Num2)
# მომხმარებელს შემოვატანინეთ ორი რიცხვი და შემდეგ ავტომატურად დავუპრინტეთ მათ შორის განხორციელებული მათემატიკური ოპერაციების შედეგი


# 6) Paint-ის საშუალებით შექმენით წრიული დიაგრამა, სადაც გექნებათ სამი კატეგორია: Input, Output და საერთო. Input-ში ჩასვით ყველა ის მოწყობილობა, რომლებიც Input-ის მაგალითია, Output-ში ის მოწყობილობები ჩასვით, რომლებიც Output-ის მაგალითებია, ხოლო საერთო კატეგორიაში ჩაწერეთ მოწყობილობები, რომლებიც როგორც Input-ს ასევე Output-საც ეკუთვნის. (Paint-ში დახატული დიაგრამა დასქრინეთ და გადაიტანეთ Day 08 homework ფოლდერში.)
# ✅