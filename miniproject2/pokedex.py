import csv


# so let's define the list outside of the loop
hp= []
with open("pokedex.txt") as pokecsv:
    for x in csv.DictReader(pokecsv):
        print(f'{x["Name"]} has an score of {x["HP"]}.')
        #hp=[]  # what's happening is that during every for loop,
               # hp is set back to being an empty list
        hp.append(x["HP"])
    # and then print the list when the loop is over
    # if we use the max() function, we can return the highest value from that huge list
    print("The Max power of Pokemon "+max(hp)+"!!")
