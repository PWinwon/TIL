import java.io.*;
import java.util.*;


public class BOJ_1043 {
	static int N;
	static int trueCnt;
	
	static int[] parents;
	static ArrayList<Integer>[] party;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int answer = 0;
		
		N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		party = new ArrayList[M];
		parents = new int[N+1];
		int[] truePeople = new int [N+1];
		
		
		for (int i = 0; i < N+1; i++) {
			parents[i] = i;
		}
		
		st = new StringTokenizer(br.readLine());
		trueCnt = Integer.parseInt(st.nextToken());		
		
		for (int i = 0; i < trueCnt; i++) {
			int idx = Integer.parseInt(st.nextToken());
			truePeople[i] = idx;
		}
		
		for (int m = 0; m < M; m++) {
			party[m] = new ArrayList<Integer>();
			st = new StringTokenizer(br.readLine());
			int partySize = Integer.parseInt(st.nextToken());
			
			for (int i = 0; i < partySize; i++) {
				party[m].add(Integer.parseInt(st.nextToken()));
			}
		}
		
		for (int i = 0; i < M; i++) {
			int temp = party[i].get(0);
			for (int j = 1; j < party[i].size(); j++) {
				union(temp, party[i].get(j));
			}
		}
		
		for (int i = 0; i < M; i++) {
			boolean flag = true;
			int temp = party[i].get(0);
			for (int j = 0; j < truePeople.length; j++) {
				if (find(temp) == find(truePeople[j])) {
					flag = false;
					break;
				}
			}
			if (flag) answer++; 
		}
		
		System.out.println(answer);
	}
	
	public static int find(int x) {
		if (parents[x] == x) {
			return x;
		}	
		
		return parents[x] = find(parents[x]);
	}
	
	public static void union(int x, int y) {
		x = find(x);
		y = find(y);
		
		if (x < y) {
			parents[y] = x;
		}
		else {
			parents[x] = y;
		}
	}
}
