example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

def split_string(source,splitlist):
	output=[]	
	atsplit=True #at split point
	for char in source :#iterate through string by each letter
		if char in splitlist:
			atsplit=True
		else:
			if atsplit:
				output.append(char)
				atsplit = False
			else:
				#add character to last word
				output[-1]=output[-1]+char		
	return output


def get_next_user(string_input):	
	#find user

	start=string_input.find(" ")
	if start==-1:
		return None,None,None,0
	name=string_input[:start]
	
	#find users connection
	con=string_input.find('to')
	end_con=string_input.find('.')
	raw_connection=string_input[con+2:end_con]
	connection=split_string(raw_connection," ,")
	
	#find users games
	game_start=string_input.find('play')
	endpos=string_input.find('.',game_start)

	raw_game=string_input[game_start+5:endpos]
	game_list=raw_game.split(", ")

	return name ,connection, game_list,endpos



def create_data_structure(string_input):
	network={}
	if string_input==" ":
		return network
	while True:
		name,connection,game_list,endpos = get_next_user(string_input)
		if connection:
			network[name]=[connection]
			network[name].append(game_list)
			string_input = string_input[endpos+1:]
		else:
			break
	return network

def get_connections(network, user):
	try:
		if network[user]:
			return network[user][0]
		else:
			return []
	except:
		return None

#print(get_connections(network,"Bryant"))

def get_games_liked(network,user):
    try:
    	if network[user]:
    		return network[user][1]
    	else:
    		return []
    except:
    	return None		

#print(get_games_liked(network,"Robin"))

def add_connection(network, user_A, user_B):
	try:
		if network[user_A] and network[user_B]:
			if user_B not  in network[user_A][0]:
				network[user_A][0].append(user_B)
				return network
		return network		
	except:
		return False	

#add_connection(network,"John","paresh")
#print(network)

def add_new_user(network, user, games):
	try:
		if network[user]:
			return network
	except:
		network[user]=[]
		network[user].append([])
		network[user].append(games)
		return network 

#print (add_new_user(network, "Nick", ["Seven Schemers", "The Movie: The Game"]))
#print(network)		

def get_secondary_connections(network, user):
	output=[]
	if network[user]:
		for u in network[user][0]:
			for us in network[u][0]: 
				if us not in output:
					output.append(us)
					
		return output
	return None

#print(get_secondary_connections(network,"paresh"))	

def count_common_connections(network, user_A, user_B):
	count=0
	try:
		for u in network[user_A][0]:
			if u in network[user_B][0]:
				count=count+1
		return count
	except:
		return False	
#print(count_common_connections(net,"Freda","John"))		

network = create_data_structure(example_input)
# network = add_new_user(network, 'Alice', [])
print(network)
# network = add_new_user(network, "Bob", [])
# print(network)
# network = add_connection(network, 'Alice', 'Bob')
# print(network)
# network = add_connection(network, 'Alice', 'Bob')
# print(network)
# print (get_connections(network, 'Alice'))

def find_path_to_friend(network, user_A, user_B,path=None):
    if path is None:
        path=[]
    path = path + [user_A]
    if user_A == user_B:
        return path
    if user_A not in network:
        return None
    for node in network[user_A][0]:
        if node not in path:
            newpath = find_path_to_friend(network, node, user_B,path)
            if newpath: return newpath
    return None


#print(find_path_to_friend(network,"John","Ollie"))