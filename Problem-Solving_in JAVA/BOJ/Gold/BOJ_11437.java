import java.io.*;
import java.util.*;


public class BOJ_11437 {
	static int N;
	static ArrayList<Integer>[] Map;
	
	static mData[] nodes;
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		
		Map = new ArrayList[N+1];
		nodes = new mData[N+1];
		
		for (int i = 0; i <= N; i++) {
			Map[i] = new ArrayList<Integer>();
		}
		
		for (int n = 0; n < N-1; n++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			Map[a].add(b);
			Map[b].add(a);
		}
		
		setNodes(1);
		
		int M = Integer.parseInt(br.readLine());
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			System.out.println(getParent(a, b));
		}
	}
	
	public static int getParent(int a, int b) {
		int ret = -1;
		
		// a > b 라면 a와 b 스왑
		if (nodes[a].depth > nodes[b].depth) {
			int swap = a;
			a = b;
			b = swap;
		}
		
		// a와 b의 깊이가 같을때까지
		while (nodes[a].depth != nodes[b].depth) {
			b = nodes[b].prt;
		}
		
		while (a != b) {
			a = nodes[a].prt;
			b = nodes[b].prt;
		}
		
		ret = a;
		
		return ret;
	}
	
	public static void setNodes(int i) {
		
		nodes[i] = new mData(0, 0);
		
		ArrayDeque<mData> que = new ArrayDeque<mData>();
		boolean[] used = new boolean[N+1];
		que.add(new mData(i, 0));
		used[1] = true;
		
		while (!que.isEmpty()) {
			mData now = que.pollFirst();
			int idx = now.prt;
			int depth = now.depth;
			
			for (int next : Map[idx]) {
				if (used[next]) continue;
				que.add(new mData(next, depth+1));
				nodes[next] = new mData(idx, depth+1);
				used[next] = true;
			}
		}
	}

}

class mData {
	int prt;
	int depth;
	
	mData(int p, int d) {
		this.prt = p;
		this.depth = d;
	}
}
