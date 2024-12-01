siz = int(input().strip())
books = []
for i in range(siz):
    books.append(input().strip())

books.sort()
for x in books:
    print(x)