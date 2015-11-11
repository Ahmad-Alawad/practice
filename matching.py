import random

class Tile(object):
  def __init__(self,kind, name, imageurl):
    self.kind = kind
    self.name = name
    self.imageurl = imageurl

walrus = Tile("walrus", "walrus", "url")
babywalrus = Tile("walrus", "baby walrus", "url")
tiger = Tile("tiger", "tiger", "url")
babytiger = Tile("tiger", "baby tiger", "url")
narwhal = Tile("narwhal", "narwhal", "url")
babynarwhal = Tile("narwhal", "baby narwhal", "url")
orangutan = Tile("orangutan", "orangutan", "url")
babyorangutan = Tile("orangutan", "baby orangutan", "url")
robin = Tile("robin", "robin", "url")
babyrobin = Tile("robin", "baby robin", "url")
dog = Tile("dog", "dog", "url")
babydog = Tile("dog", "baby dog", "url")
iguana = Tile("iguana", "iguana", "url")
babyiguana = Tile("iguana", "baby iguana", "url")
cow = Tile("cow", "cow", "url")
babycow = Tile("cow", "baby cow", "url")

cards = [
walrus,
babywalrus, 
tiger,
babytiger,
narwhal,
babynarwhal,
orangutan,
babyorangutan,
robin,
babyrobin,
dog,
babydog,
iguana,
babyiguana,
cow,
babycow
]


def print_grid(grid, matched):
    characters =[]
    for x in range (1, len(grid) + 1):
        if x in matched:
            characters.append("*")
        else:
            characters.append(x)
    print "^^^^^^^^^^^^^ Thanks for coming Christin ^^^^^^^^^^^^^^^^^^^^^" 
    print "******************************************"
    print "* Match the parent with the baby animal! *"
    print "******************************************"
    print "-------------------"
    print " %s  | %s  | %s  | %s " % (characters[0], characters[1], characters[2], characters[3])
    print "-------------------"
    print " %s  | %s  | %s  | %s" % (characters[4], characters[5], characters[6], characters[7])
    print "-------------------"
    print " %s  | %s | %s | %s" % (characters[8], characters[9], characters[10], characters[11])
    print "-------------------"
    print " %s | %s | %s | %s" % (characters[12], characters[13], characters[14], characters[15])
    print "-------------------"

def play():
    matched = []
    grid = random.sample(cards, len(cards))
    while True:
        print_grid(grid, matched)
        if len(matched) == len(grid):
            print "You have matched all the animals!"
            break

        while True:
            i = int(raw_input("choose a numbered tile!"))
            if i not in matched:
                print "You picked %s" %grid[i-1].name
                break
            else:
                print "This number in unavailable, pick again."
                    
        while True: 
            k = int(raw_input("choose another numbered tile!"))
            if k == i:
                print "Sorry, you cannot guess the same tile twice."
            if k not in matched:
                print "You picked %s" %grid[k-1].name
                break
            else:
                print "This number in unavailable, pick again."

        if k != i and grid[i-1].kind == grid[k-1].kind:
            matched.append(k)
            matched.append(i)
            print "it's a match!"
        else:
            if grid[i-1].kind != grid[k-1].kind:
                print "Sorry, these tiles aren't a match"


while True:
    play()
    y = raw_input("Want to play again? (y/n)")
    if y != "y":
        break




  
    

