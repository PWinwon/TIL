import java.io.*;
import java.util.*;


public class BOJ_17472 {
	static int[] dr = {-1, 1, 0, 0};
	static int[] dc = {0, 0, -1, 1};
	
	static int R, C, landNum;
	static int[][] Map;
	static boolean[][] visited;
	
	static ArrayList<ArrayList<Point>> pointList;
	static ArrayList<Point> pList;

	static PriorityQueue<Edge> pq;
	
	static int[] parents;
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		
		Map = new int[R][C];
		visited = new boolean[R][C];
		
		for (int r = 0; r < R; r++) {
			st = new StringTokenizer(br.readLine());
			for (int c = 0; c < C; c++) {
				Map[r][c] = Integer.parseInt(st.nextToken());
			}
		}
		
		landNum = 1;
		pointList = new ArrayList<>();
		
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				if (!visited[r][c] && Map[r][c] == 1) {
					myBFS(r, c);
					pointList.add(pList);
					landNum++;
				}
			}
		}
		
		
		pq = new PriorityQueue<Edge>();
		
		for (int i = 0; i < pointList.size(); i++) {
			ArrayList<Point> now = pointList.get(i);
			
			for (int j = 0; j < now.size(); j++) {
				int y = now.get(j).y;
				int x = now.get(j).x;
				int d = now.get(j).d;
				int l = 1;
				
				while (y + dr[d] >= 0 && y + dr[d] < R && x + dc[d] >= 0 && x + dc[d] < C) {
					y += dr[d];
					x += dc[d];
					if (Map[y][x] == i+1) break;
					else if (Map[y][x] == 0) l++;
					else {
						if (l > 1) pq.add(new Edge(i+1, Map[y][x], l));
						break;
					}
				}
			}
		}
		
		int de = -1;
		
		parents = new int[landNum];
		for (int i = 0; i < landNum; i++) {
			parents[i] = i;
		}
		
		int edgeCnt = 0;
		int answer = 0;
		
		while (!pq.isEmpty()) {
			Edge now = pq.poll();
			if (find(now.start) == find(now.end)) continue;
			union(now.start, now.end);
			answer += now.cost;
			edgeCnt++;
		}
		
		if (edgeCnt == landNum - 2) {
			System.out.println(answer);
		}
		else {
			System.out.println(-1);
		}
		
		
//		for (int i = 0; )
		
//		for (int r = 0; r < R; r++) {
//			for (int c = 0; c < C; c++) {
//				System.out.print(Map[r][c] + " ");
//			}
//			System.out.println();
//		}

	}
	
	public static int find(int x) {
		if (x == parents[x]) return x;
		return parents[x] = find(parents[x]);	
	}
	
	public static void union(int x, int y) {
		x = find(x);
		y = find(y);
		if (x > y) parents[x] = y;
		else parents[y] = x;
	}
	
	public static void myBFS(int r, int c) {
		pList = new ArrayList<Point>();
		
		ArrayDeque<Point> que = new ArrayDeque<Point>();
		que.add(new Point(r, c));
		visited[r][c] = true;
		Map[r][c] = landNum;
		
		while (!que.isEmpty()) {
			Point p = que.pollFirst();
			for (int i = 0; i < 4; i++) {
				int yr = p.y + dr[i];
				int xr = p.x + dc[i];
				
				if (yr < 0 || yr >= R || xr < 0 || xr >= C) continue;
				if (visited[yr][xr]) continue;
				if (Map[yr][xr] == 0) pList.add(new Point(yr, xr, i));
				else {
					que.add(new Point(yr, xr));
					visited[yr][xr] = true;
					Map[yr][xr] = landNum;
				}
			}
		}
	}
	
	static class Point {
		int y;
		int x;
		int d;
		
		Point(int y, int x) {
			this.y = y;
			this.x = x;
		}
		
		Point(int y, int x, int d) {
			this.y = y;
			this.x = x;
			this.d = d;
		}
	}
	
	static class Edge implements Comparable<Edge> {
		int start;
		int end;
		int cost;
		
		Edge(int s, int e, int c) {
			this.start = s;
			this.end = e;
			this.cost = c;
		}
		
		@Override
		public int compareTo(Edge o) {
			return this.cost - o.cost;
		}
	}
}
