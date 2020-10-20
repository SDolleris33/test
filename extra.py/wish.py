books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]

def display_wish(display_name,wishes):
	items = wishes.copy()
	print(display_name +':')
	suggested_gift = items.pop(0)
	print('>>>>',suggested_gift,'<<<<')
	for wish in wishes:
		print('* ' + wish)
	print()
	
display_wish('Books', books)
display_wish('Video Games', video_games)
display_wish('Video Games', video_games)

