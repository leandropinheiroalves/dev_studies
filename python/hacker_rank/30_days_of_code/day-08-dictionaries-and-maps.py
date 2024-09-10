'''https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem?isFullScreen=true'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
phone_book = {}
for i in range(n):
    contact = input().split()
    phone_book[contact[0]] = contact[1]

while True:
    try:
        search = input()
        if search in phone_book:
            print(f'{search}={phone_book[search]}')
        else:
            print('Not found')
    except:
        break

