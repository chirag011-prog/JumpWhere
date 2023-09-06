#The Penalty Shootout
def penaltyScore(S):
	# code here
	c = 0
	for i in range(len(S)-1):
		if S[i] == '2' and S[i+1] == '1':
			c+=1
			continue
	return c
S = input()
print(penaltyScore(S))
 # 1 = goal
 # 0 no goal
 # 2 penalty goal
 # i/p 1012012112110
 # o/p 2