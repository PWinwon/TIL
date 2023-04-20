import java.io.*;
import java.util.*;


public class BOJ_2251 {
	
	// 주는 물통, 받는 물통 정하기..?
	static int[] send = {0, 0, 1, 1, 2, 2};
	static int[] rece = {1, 2, 0, 2, 0, 1};
	
	// 물통 visited
	static boolean[][] visited;
	static ArrayDeque<int[]> que;

	// 물통 용량 고정?
	static int[] volume = new int[3];
	
	static boolean[] answer;
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < 3; i++) {
			volume[i] = Integer.parseInt(st.nextToken());
		}
		
		que = new ArrayDeque<int[]>();
		visited = new boolean [volume[0]+1][volume[1]+1];
	
		answer = new boolean[volume[2]+1];
		
		que.add(new int[] {0, 0, volume[2]});
		visited[0][0] = true;
		answer[volume[2]] = true;
		
		while (!que.isEmpty()) {
			int[] now = que.pollFirst();
			for (int i = 0; i < 6; i++) {
				int temp[] = pourWater(send[i], rece[i], now);
				if (visited[temp[0]][temp[1]]) {
					continue;
				}
				if (temp[0] == 0) {
					answer[temp[2]] = true;
				}
				visited[temp[0]][temp[1]] = true;
				que.add(temp);
				// a가 0일때
			}
		}
		
		for (int i = 0; i < volume[2]+1; i++) {
			if (answer[i]) {
				System.out.print(i + " ");
			}
		}
	}
	
	public static int[] pourWater(int a, int b, int[] w) {
		// a, b는 물통 idx이다.
		// a의 물을 b로 비워야한다.
		// a에 들어있는 물의양 w[a]
		// b에 들어있는 물의양 w[b]
		// b물통 용량 volume[b]
		// w[a] + w[b] <= volume[b] 를 만족하면 그냥 부어주고 a는 0으로 초기화
		// w[a] + w[b] > volume[b] 이면, b를 가득채우고 남는 만큼 남겨두기
		int[] ret = new int[3];
		for (int i = 0; i < 3; i++) {
			ret[i] = w[i];
		}
		if (ret[a] + ret[b] <= volume[b]) {
			ret[b] += ret[a];
			ret[a] = 0;
		}
		else {
			ret[a] -= volume[b] - ret[b];
			ret[b] = volume[b];
		}
		
		return ret;
	}

}
