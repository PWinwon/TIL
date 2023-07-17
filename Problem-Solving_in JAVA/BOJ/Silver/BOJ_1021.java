import java.io.*;
import java.util.*;


public class BOJ_1021 {
	
	static ArrayDeque<Integer> que = new ArrayDeque<Integer>();

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int answer = 0;
		
		
		for (int i = 1; i <= N; i++) {
			que.add(i);
		}
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < M; i++) {
			int idx = getIdx(Integer.parseInt(st.nextToken()));
			
			if (idx > N / 2) {
				idx = N - idx;
				moveBack(idx);
				answer += idx;
			}
			else {
				moveFront(idx);
				answer += idx;
			}
			
			que.pollFirst();
			N--;
			
//			System.out.println(idx);
			
		}

		System.out.println(answer);
	}
	
	public static void moveBack(int cnt) {
		while (cnt > 0) {
			que.addFirst(que.pollLast());
			cnt--;
		}
	}
	
	public static void moveFront(int cnt) {
		while (cnt > 0) {
			que.add(que.pollFirst());
			cnt--;
		}
	}
	
	public static int getIdx(int n) {
		int ret = 0;
		
		for (int num : que) {
			if (num == n) return ret;
			ret++;
		}
		
		return -1;
	}

}
