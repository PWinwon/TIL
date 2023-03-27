import java.io.*;
import java.util.*;


public class BOJ_1260 {
	static ArrayList<Integer>[] myMap;
	static ArrayList<Integer> dfsAnswer;
	static boolean[] used;
	static int[] bfsAnswer;
	static int N;
	static boolean dfsFlag;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		
		N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int V = Integer.parseInt(st.nextToken());
		
		myMap = new ArrayList[N+1];
		used = new boolean[N+1];
		dfsAnswer = new ArrayList<Integer>();
		bfsAnswer = new int [N];
		
		for (int n = 1; n <= N; n++) {
			myMap[n] = new ArrayList<Integer>();
		}
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			myMap[a].add(b);
			myMap[b].add(a);
		}
		
		for (int n = 1; n <= N; n++) {
			Collections.sort(myMap[n]);
		}
		
		dfsAnswer.add(V);
		used[V] = true;
		myDFS(1, V);
		
		Deque<Integer> deque = new ArrayDeque<>();
		used = new boolean [N+1];
		
		deque.offer(V);
		used[V] = true;
		
		int bfsNow = -1;
		int cnt = 0;
		
		while (!deque.isEmpty()) {
			bfsNow = deque.pollFirst();
			bfsAnswer[cnt] = bfsNow;
			cnt++;
			for (int i : myMap[bfsNow]) {
				if (used[i]) {
					continue;
				}
				used[i] = true;
				deque.offerLast(i);				
			}
		}
		
		for (int i = 0; i < dfsAnswer.size(); i++) {
			sb.append(dfsAnswer.get(i)).append(" ");
		}
		sb.append("\n");
		
		for (int i = 0; i < N; i++) {
			if (bfsAnswer[i] == 0) {
				break;
			}
			sb.append(bfsAnswer[i]).append(" ");
		}
		System.out.print(sb);
	}
	
	public static void myDFS(int depth, int now) {
//		if (depth == N || dfsFlag) {
//			dfsFlag = true;
//			return;
//		}
//		used[now] = true;
		for (int i : myMap[now]) {
			if (used[i]) {
				continue;
			}
			dfsAnswer.add(i);
			used[i] = true;
			myDFS(depth+1, i);
		}
//		used[now] = false;
	}

}
