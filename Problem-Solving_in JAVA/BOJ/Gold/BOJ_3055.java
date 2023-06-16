import java.io.*;
import java.util.*;


public class BOJ_3055 {
	static int R, C;
	static int[] dr = {-1, 1, 0, 0};
	static int[] dc = {0, 0, -1, 1};
	static char[][] Map;
	static boolean[][] visited;
	static ArrayDeque<Node> que = new ArrayDeque<Node>();
	static ArrayDeque<Node> water = new ArrayDeque<Node>();
	static Node goal;
	static int answer = -1;
	static boolean flag = false;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		
		Map = new char[R][C];
		visited = new boolean[R][C];
		
		
		// 비어있는 곳 '.', 물 '*', 돌은 'X', 비버의 굴'D', 고슴도치'S'
		for (int r = 0; r < R; r++) {
			char[] temp = br.readLine().toCharArray();
			for (int c = 0; c < C; c++) {
				Map[r][c] = temp[c];
				switch (temp[c]) {
					case '*' :
						water.add(new Node(r, c));
						break;
					case 'D' :
						goal = new Node(r, c);
						break;
					case 'S' :
						que.add(new Node(r, c, 0));
						visited[r][c] = true;
						Map[r][c] = '.';
						break;
					default :
						break;
				}
			}
		}
		
		while (!que.isEmpty()) {
			// 물 먼저 이동
			waterMove();
			// 고슴 도치 이동
			dotchMove();
			if (flag) break;
		}
		
		if (flag) System.out.println(answer);
		else System.out.println("KAKTUS");

	}
	public static void dotchMove() {
		ArrayDeque<Node> newQue = new ArrayDeque<Node>();
		
		while (!que.isEmpty()) {
			if (flag) break;
			Node now = que.pollFirst();
			int r = now.r;
			int c = now.c;
			for (int i = 0; i < 4; i++) {
				int yr = r + dr[i];
				int xr = c + dc[i];
				if (rangeChk(yr, xr)) continue;
				// 이미 방문한 곳이면 continue
				if (visited[yr][xr]) continue;
				// 물이 차있는 곳이면 continue
				if (Map[yr][xr] == '*' || Map[yr][xr] == 'X') continue;
				// 도착점과 같다면
				if (yr == goal.r && xr == goal.c) {
					flag = true;
					answer = now.t+1;
				}
				newQue.add(new Node(yr, xr, now.t+1));
				visited[yr][xr] = true;
			}
		}
		
		que = newQue;
	}
	
	public static boolean rangeChk(int y, int x) {
		if (y < 0 || y >= R || x < 0 || x >= C) return true;
		return false;
	}
	
	public static void waterMove() {
		ArrayDeque<Node> newWater = new ArrayDeque<Node>();
		
		while (!water.isEmpty()) {
			Node now = water.pollFirst();
			int r = now.r;
			int c = now.c;
			for (int i = 0; i < 4; i++) {
				int yr = r + dr[i];
				int xr = c + dc[i];
				if (rangeChk(yr, xr)) continue;
				if (Map[yr][xr] == '.') {
					newWater.add(new Node(yr, xr));
					Map[yr][xr] = '*';
				}
				
			}
		}
		water = newWater;
	}

}

class Node {
	int r;
	int c;
	int t;
	Node(int r, int c) {
		this.r = r;
		this.c = c;
	}
	
	Node(int r, int c, int t) {
		this.r = r;
		this.c = c;
		this.t = t;
	}
}
