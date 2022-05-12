import math

#Theoritical probabilities
n_S = math.comb(52,7)

n_4 = math.comb(4,4) * math.comb(48,3)
#probability that hand of 7 cards contains all the kings
Pr_1 = n_4/n_S
print(Pr_1)

n_3 = math.comb(4,3) * math.comb(48,4)
#probability that hand of 7 cards contains 3 kings
Pr_2 = n_3/n_S
print(Pr_2)

#probability that hand of 7 cards contains atleast 3 kings
Pr_3 = Pr_1+Pr_2
print(Pr_3)

