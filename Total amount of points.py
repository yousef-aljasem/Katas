def points(games):
    total = 0
    for position, value in enumerate(games):
        splitting = games[position].split(":")
        print(position, value, splitting)
        if(int(splitting[0]) > int(splitting[1])):
            total += 3
            print(total)
        elif(int(splitting[0]) == int(splitting[1])):
            total += 1
            print(total)
    return total
        
