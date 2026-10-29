prices_books = [100,200,450,800,550,1000,2500,299,779,889,333,80,120,150,160]
def sort_prices(a):
	if len(a) <= 1:
		return a

	q = len(a) // 2 

	left = sort_prices(a[:q])
	right = sort_prices(a[q:])
	return merge(left, right)

def merge(L, R):
	out, i, j = [], 0, 0
	while i < len(L) and j < len(R):
		if L[i] <= R[j]:
			out.append(L[i]);i += 1
		else:
			out.append(R[j]);j += 1
	return out + L[i:] + R[j:]

def search_by_price(arr, s):
	if len(arr):
		if s == arr[-1]:
			return True
		else:
			return search_by_price(arr[:-1], s)
	else:
		return False

	

print("Book you")
print("Hello " + input("You'r Name? ")) 
print("Prices: " + str(sort_prices(prices_books)))

salary = int(input("Enter Salary: "))

if search_by_price(prices_books, salary):
	print("Found")
else:
	print("Go to Work, You'r is homeless")
