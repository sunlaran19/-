
score=0

print("Ответь на мои вопросы:")

question = ["Как называется (обычно белый) конь с крыльями?","Как называется дева с хвостом?","Как называется  (обычно белый) конь с рогом?","Как называется конь с телом человека?","Как называется огромный осьминог топящий корабли?","Как называется одноглазый великан?","Как называется крылатый лев с головой орла?","Как звали самого главного бога на Олимпе?","Как звали посланца богов в крылатых сандалях?","Как называли детей с крльями?"]

answer = ["пегас","русалка","единорог","кентавр ","кракен","циклоп","грифон","Зевс","Гермес","ангел"]
print(question[0])

User_1 =input("введите ответ ")
if User_1==answer[0]:
  print("ВЕРНО!:)")
  score=score+1
else:
  print("НЕ ВЕРНО!:( правельный ответ")

print(question[1])

User_1 =input("введите ответ ")
if User_1==answer[1]:
  print("ВЕРНО!:)")
  score+=1
else:
  print("НЕ ВЕРНО!:(")
  print(question[1])

  User_1 =input("введите ответ ")
  if User_1==answer[2]:
    print("ВЕРНО!:)")
    score+=1
  else:
    print("НЕ ВЕРНО!:(")

print(question[2])

User_1 =input("введите ответ ")
if User_1==answer[3]:
  print("ВЕРНО!:)")
  score+=1
else:
  print("НЕ ВЕРНО!:(")

print(question[3])

User_1 =input("введите ответ ")
if User_1==answer[4]:
  print("ВЕРНО!:)")
else:
  print("НЕ ВЕРНО!:(")

print(question[4])

User_1 =input("введите ответ ")
if User_1==answer[5]:
  print("ВЕРНО!:)")
else:
  print("НЕ ВЕРНО!:(")

print(question[5])

User_1 =input("введите ответ ")
if User_1==answer[6]:
  print("ВЕРНО!:)")
else:
  print("НЕ ВЕРНО!:(")

print(question[6])

User_1 =input("введите ответ ")
if User_1==answer[7]:
  print("ВЕРНО!:)")
else:
  print("НЕ ВЕРНО!:(")

print(question[7])

User_1 =input("введите ответ ")
if User_1==answer[8]:
  print("ВЕРНО!:)")
else:
  print("НЕ ВЕРНО!:(")

print(question[8])

User_1 =input("введите ответ ")
if User_1==answer[9]:
  print("ВЕРНО!:)")
else:
  print("НЕ ВЕРНО!:(")

print(question[9])

User_1 =input("введите ответ ")
if User_1==answer[10]:
  print("ВЕРНО!:)")
else:
  print("НЕ ВЕРНО!:(")

print(question[10])

print("вы набрали  ", score)