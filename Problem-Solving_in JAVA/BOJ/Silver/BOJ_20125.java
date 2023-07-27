import java.io.*;
import java.util.*;


public class BOJ_20125 {
	static int N;
	
	// 상 하 좌 우 좌하 우하
	static int[] dr = {-1, 1, 0, 0, 1, 1};
	static int[] dc = {0, 0, -1, 1, -1, 1};
	
	static char[][] myMap;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		int[] answer = new int[5];
		
		myMap = new char[N][N];		
		
		for (int r = 0; r < N; r++) {
			char[] temp = br.readLine().toCharArray();
			for (int c = 0; c < N; c++) {
				myMap[r][c] = temp[c];
			}
		}
		
		int[] heart = new int[2];
		
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < N; c++) {
				if (chkHeart(r, c)) {
					heart[0] = r;
					heart[1] = c;
					break;
				}
			}
		}
		
		answer[0] = getLength(heart[0], heart[1], 2);
		answer[1] = getLength(heart[0], heart[1], 3);
		answer[2] = getLength(heart[0], heart[1], 1);
		
		// 허리 끝 좌표
		int[] hury = new int[2];
		hury[0] = heart[0] + dr[1] * answer[2];
		hury[1] = heart[1] + dc[1] * answer[2];
		
//		System.out.println(hury[0] + " " + hury[1]);
		
		answer[3] = getLength(hury[0], hury[1]-1, 1);
		answer[4] = getLength(hury[0], hury[1]+1, 1);
		
		heart[0]++;
		heart[1]++;
		
		System.out.println(heart[0]+ " " + heart[1]);
		
		for (int i = 0; i < 5; i++) {
			System.out.print(answer[i] + " ");
		}
		
	}
	
	public static int getLength(int r, int c, int d) {
		int ret = 0;
		
		int sr = r + dr[d];
		int sc = c + dc[d];
		
		while (0 <= sr && sr < N && 0 <= sc && sc < N) {
			if (myMap[sr][sc] == '_') {
				break;
			}
			ret++;
			sr += dr[d];
			sc += dc[d];
		}
		
		return ret;
	}
	
	public static boolean chkHeart(int r, int c) {
		for (int i = 0; i < 4; i++) {
			int yr = r + dr[i];
			int xr = c + dc[i];
			if (yr < 0 || yr >= N || xr < 0 || xr >= N || myMap[yr][xr] == '_') return false;
		}
				
		return true;
	}

}
