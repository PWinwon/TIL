import java.io.*;
import java.util.*;

public class BOJ_13023 {
	
	static ArrayList<Integer>[] fList;
	static boolean[] used;
	static int N;
	static int M;
	static boolean flag = false;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		fList = new ArrayList[N];
		used = new boolean[N];
		
		for (int i = 0; i < N; i++) {
			fList[i] = new ArrayList<Integer>();
		}
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			fList[a].add(b);
			fList[b].add(a);
		}
		
		for (int n = 0; n < N; n++) {
			if (flag) {
				break;
			}
			used[n] = true;
			myDFS(1, n);
			used[n] = false;
		}
		
		int de = -1;
		
		if (flag) {
			System.out.print(1);
		}
		else {
			System.out.print(0);
		}
	}
	
	public static void myDFS(int d, int x) {
		if (flag) {
			return;
		}
		if (d == 5) {
			flag = true;
			return;
		}
		for (int i : fList[x]) {
			if (used[i]) {
				continue;
			}
			used[i] = true;
			myDFS(d+1, i);
			used[i] = false;
		}
		return;
	}

}
