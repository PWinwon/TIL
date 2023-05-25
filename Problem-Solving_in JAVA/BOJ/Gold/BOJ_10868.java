import java.io.*;
import java.util.*;


public class BOJ_10868 {
	static int N, M, treeL;
	
	static long[] tree;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		treeL = getL(N);
		int sIdx = treeL / 2 - 1;
		
		tree = new long[treeL];
		
		for (int i = 0; i < treeL; i++) {
			tree[i] = Integer.MAX_VALUE;
		}
		
		for (int i = sIdx+1; i <= sIdx + N; i++) {
			tree[i] = Long.parseLong(br.readLine());
		}
		
		setTree(treeL - 1);
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken()) + sIdx;
			int e = Integer.parseInt(st.nextToken()) + sIdx;
			System.out.println(myMin(s, e));
		}
		
//		printTree();
	}
	
	public static long myMin(int s, int e) {
		long ret = Long.MAX_VALUE;
		while (s <= e) {
			if (s % 2 == 1) {
				ret = Math.min(ret, tree[s]);
				s++;
			}
			if (e % 2 == 0) {
				ret = Math.min(ret, tree[e]);
				e--;
			}
			s /= 2;
			e /= 2;
		}
		return ret;
	}
	
	public static void setTree(int i) {
		while (i != 1) {
			if (tree[i / 2] > tree[i])	tree[i / 2] = tree[i];
			i--;
		}
	}
	
	public static int getL(int n) {
		int ret = 2;
		while (ret < n) {
			ret *= 2;
		}
		return ret * 2;
	}
	
	public static void printTree() {
		for (int i = 0; i < treeL; i++) {
			System.out.print(tree[i] + " ");
		}
	System.out.println();
}

}
