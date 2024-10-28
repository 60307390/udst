import math

# --- Part a) ---

A = set()
for i in range(1,1000):   # Interval: [1,1000) (Z+)
    last_digits = (i//10 % 10)*10 + i%10   # Get last two digits 
    if i < 10:  # If single digit number
        last_digits = i 
    if last_digits % 43 == 0:
        A.add(i)

# print(186 in A) # OK

# --- Part b) ---

B = set()
for i in range(1,1000):
    if i >= 10:
        k = math.floor(math.log10(i))   # Get power of 10 for i
        first_digits = (i//10**k)*10 + (i//10**(k-1)%10)    # Get 2 digits using k
    else:
        first_digits = i
    if first_digits % 24 == 0:
        B.add(i)

# print(72 in B)    # OK

# --- Part c) ---

C = set()
for x in A:
    C.add(x)
for x in B:
    C.add(x)

# OR
# C = A|B

# --- Part d) ---

D = set()
for x in C:
    if x in A and x in B:
        D.add(x)

# OR
# D = A&B

# --- Part e) ---

print(len(A) + len(B) == len(C) + len(D))

# --- Part f) ---

def cartesian(A, B):
    cartesian_product = set()
    for i in A:
        for j in B:
            cartesian_product.add((i,j))
    return cartesian_product

# print(cartesian(set([1,2,3]), set(['a','b','c']))) OK

# --- Part g) ---
print(cartesian(D, set(['RED','YELLOW','GREEN'])))
