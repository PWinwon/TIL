import java.io.*;
import java.util.*;


public class BOJ_18430 {
	static int R, C, answer;
	static int[][] Map;
	static boolean[][] visited;
	
	// 좌, 하, 우, 상, 좌
	static int[] dr = {0, 1, 0, -1, 0};
	static int[] dc = {-1, 0, 1, 0, -1};

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
		
		answer = 0;
		
		myFunc(0, 0);
		System.out.println(answer);

	}
	
	public static void myFunc(int n, int total) {
		if (n == R * C) {
			if (total > answer) answer = total;
			return;
		}
		
		int r = n / C;
		int c = n % C;
		
		// 해당 칸이 부메랑으로 사용되지 않은 경우
		if (!visited[r][c]) {			
			for (int i = 0; i < 4; i++) {
				int yr1 = r + dr[i];
				int xr1 = c + dc[i];
				int yr2 = r + dr[i+1];
				int xr2 = c + dc[i+1];
				if (checkRange(yr1, xr1, yr2, xr2)) continue;
				if (visited[yr1][xr1] || visited[yr2][xr2]) continue;
				
				visited[r][c] = true;
				visited[yr1][xr1] = true;
				visited[yr2][xr2] = true;
				
				myFunc(n+1, total + getSum(r, c, i));
				
				visited[r][c] = false;
				visited[yr1][xr1] = false;
				visited[yr2][xr2] = false;
				
			}
		}
		myFunc(n+1, total);
		return;
	}
	
	public static int getSum(int r, int c, int i) {
		return Map[r][c] * 2 + Map[r+dr[i]][c+dc[i]] + Map[r+dr[i+1]][c+dc[i+1]];
	}
	
	public static boolean checkRange(int yr1, int xr1, int yr2, int xr2) {
		if (yr1 < 0 || yr1 >= R) return true;
		else if (yr2 < 0 || yr2 >= R) return true;
		else if (xr1 < 0 || xr1 >= C) return true;
		else if (xr2 < 0 || xr2 >= C) return true;
		return false;
	}

}
