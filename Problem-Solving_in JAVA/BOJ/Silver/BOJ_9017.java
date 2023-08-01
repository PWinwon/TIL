import java.io.*;
import java.util.*;


public class BOJ_9017 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 0; tc < T; tc++) {
			int N = Integer.parseInt(br.readLine());
			
			int[] board = new int[N];
			HashMap<Integer, Integer> myMap = new HashMap<Integer, Integer>();
			
			st = new StringTokenizer(br.readLine());
			
			for (int n = 0; n < N; n++) {
				board[n] = Integer.parseInt(st.nextToken());
				
				if (myMap.containsKey(board[n])) {
					myMap.put(board[n], myMap.get(board[n]) + 1);
					continue;
				}
				myMap.put(board[n], 1);
			}
			
			Team[] score = new Team[201];
			
			for (int i = 1; i < 201; i++) {
				score[i] = new Team(-1, -1, -1);
			}
			
			for (int teamNum : myMap.keySet()) {
				int cnt = myMap.get(teamNum);
				if (cnt == 6) score[teamNum] = new Team(0, 0, 0);
			}
			
			int rank = 1;
			
			for (int n = 0; n < N; n++) {
				int teamN = board[n];
				
				if (score[teamN].cnt == -1) continue;
				
				else if (score[teamN].cnt <= 4) {
					score[teamN].score += rank;
				}
				
				else if (score[teamN].cnt == 5) {
					score[teamN].five = rank;
				}
				
				rank++;
				score[teamN].cnt++;				
			}
			
			int answer = -1;
			int ansScore = N * 6;
			int five = N;
			
			for (int i = 1; i < 201; i++) {
				Team team = score[i];
				if (team.cnt < 6) continue;
				else if (ansScore > team.score) {
					ansScore = team.score;
					answer = i;
					five = team.five;
				}
				else if (ansScore == team.score && five > team.five) {
					answer = i;
					five = team.five;
				}
			}
			
			int de = -1;
			
			System.out.println(answer);
			
		
		}

	}

}

class Team {
	int cnt;
	int score;
	int five;
	Team (int c, int s, int f) {
		this.cnt = c;
		this.score = s;
		this.five = f;
	}
}
