import java.io.*;
import java.util.*;


public class BOJ_20006 {
	static int P, M;
	static ArrayList<Room> waitingRoom = new ArrayList<>();

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		P = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		for (int i = 0; i < P; i++) {
			st = new StringTokenizer(br.readLine());
			int level = Integer.parseInt(st.nextToken());
			String name = st.nextToken();
			// 들어갈수 있는방이 있다면 입장
			// 없다면 생성 후 입장
			boolean flag = false;
			for (int j = 0; j < waitingRoom.size(); j++) {
				Room room = waitingRoom.get(j);
				int rng = room.lev;
				int cnt = room.cnt;
				if (level <= rng + 10 && level >= rng - 10 && cnt < M) {
					// 입장 가능한 방이므로 입장
					waitingRoom.get(j).entrancePlayer(name, level);
					flag = true;
					break;
				}
			}
			
			if (flag) {
				continue;
			} else {
				waitingRoom.add(new Room(level, name));
			}
		}
		
		StringBuilder sb = new StringBuilder();
		
		for (int i = 0; i < waitingRoom.size(); i++) {
			Room room = waitingRoom.get(i);
			if (room.cnt == M) {
				sb.append("Started!\n");
			} else {
				sb.append("Waiting!\n");
			}
			
			PriorityQueue<Player> players = room.players;
			
			while(!players.isEmpty()) {
				Player p = players.poll();
				sb.append(p.lev + " " + p.name + "\n");
			}
		}
		
		System.out.print(sb.toString());

	}

}

class Player implements Comparable<Player> {
	String name;
	int lev;
	Player(String n, int l) {
		this.name = n;
		this.lev = l;
	}
	
	@Override
	public int compareTo(Player target) {
		return this.name.compareTo(target.name);
	}
}

class Room {
	int cnt;
	int lev;
	PriorityQueue<Player> players = new PriorityQueue<>();
	
	// CreateRoom
	Room(int l, String p) {
		this.cnt = 1;
		this.lev = l;
		this.players.add(new Player(p, l));
	}
	
	public void entrancePlayer(String p, int l) {
		this.cnt++;
		this.players.add(new Player(p, l));
		return;
	}
}
