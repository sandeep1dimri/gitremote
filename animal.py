import sys


def cat():
	print("meow meow!!")


def dog():
	print("woof woof!")

def default():
	print("No Animal Sound")

def main():

	if sys.argv[1]=="cat":
		cat()
	elif sys.argv[1]=='dog':
		dog()
	else:
		default()

if __name__=="__main__":
	main()



