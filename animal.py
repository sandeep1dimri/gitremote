import sys

def cat():
	print("meow meow!!")

def default():
	print("No Animal Sound")

def main():
	if sys.argv[1]=="cat":
		cat()
	else:
		default()

if __name__=="__main__":
	main()



