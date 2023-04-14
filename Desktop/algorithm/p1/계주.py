'''
String[] players = {"mumu", "soe", "poe", "kai", "mine"};
		String[] callings = {"kai", "kai", "mine", "mine"};
		ArrayList<String> player = new ArrayList<>(Arrays.asList(players));
		
		//Collections.swap(arrayList, index1, index2);
		
		for(String s : callings) {
			int index = player.indexOf(s);
			Collections.swap(player, index, index-1);
		}
		
		String[] answer = player.toArray(new String[player.size()]);
		System.out.println(answer);
'''


players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
player = list(players)

for s in callings:
    index = player.index(s)
    player[index], player[index-1] = player[index-1], player[index]

answer = player
print(answer)