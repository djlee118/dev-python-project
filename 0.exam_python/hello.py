print("hello world")

for i in [1,2,3,4]:
    print(i)

for data in range(10):
    print(data)

data =0 

while data < 10:
    print(data)
    data = data + 1


user_input = ''

while user_input != 'quit':
    user_input = input('Input: ')
    print(user_input)

    for for_data in range(100):
        print(for_data)
        if for_data %2 == 1:
            continue;

        print ("test")


import datetime
now = datetime.datetime.now()
now = now - datetime.timedelta(days=1)

