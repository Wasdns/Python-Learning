#!/usr/bin/env python3

def is_palindrome(n) :
	i, j, cnt = n, n, 0
	while i > 0 :
		cnt = cnt+1
		i = int(i/10) # hint
	ans = True
	s = str(j)
	for i in range(0, cnt) :
		if s[i] != s[cnt-1-i] :
			ans = False
			break
	return ans

def main() :
	output = filter(is_palindrome, range(1, 1000))
	print(list(output))

if __name__ == '__main__':
	main()