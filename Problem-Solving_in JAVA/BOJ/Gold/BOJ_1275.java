import java.io.*;
import java.util.*;


public class BOJ_1275 {
	static int N, Q, treeL, sIdx;
	static long[] tree;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		Q = Integer.parseInt(st.nextToken());
		
		treeL = getL(N);
		sIdx = treeL / 2 - 1;
		
		tree = new long[treeL];
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = sIdx+1; i <= sIdx + N; i++) {
			tree[i] = Integer.parseInt(st.nextToken());
		}
		
		treeSet(treeL-1);
		
		for (int i = 0; i < Q; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken()) + sIdx;
			int y = Integer.parseInt(st.nextToken()) + sIdx;
			int a = Integer.parseInt(st.nextToken());
			long b = Long.parseLong(st.nextToken());
			
			if (x > y) System.out.println(getSum(y, x));
			else System.out.println(getSum(x, y));
			
			updateTree(a + sIdx, b);
		}

	}
	
	public static void updateTree(int i, long val) {
		long diff = val - tree[i];
		
		while (i > 0) {
			tree[i] += diff;
			i /= 2;
		}
	}
	
	public static long getSum(int x, int y) {
		long ret = 0;
		
		while (x <= y) {
			if (x % 2 == 1) {
				ret += tree[x];
				x++;
			}
			if (y % 2 == 0) {
				ret += tree[y];
				y--;
			}
			x /= 2;
			y /= 2;
		}
		
		return ret;
	}
	
	public static void treeSet(int n) {
		while (n != 1) {
			tree[n / 2] += tree[n];
			n--;
		}
	}
	
	public static void printTree() {
		for (int i = 0; i < treeL; i++) {
			System.out.print(tree[i] + " ");
		}
		System.out.println();
	}
	
	public static int getL(int n) {
		int ret = 1;
		
		while (ret < n) {
			ret *= 2;
		}
		
		return ret * 2;
	}
}
