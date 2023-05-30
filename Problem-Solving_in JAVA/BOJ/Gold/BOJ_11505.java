import java.io.*;
import java.util.*;


public class BOJ_11505 {
	static int N, M, K, treeL, sIdx;
	static long[] tree;
	
	static long myMod = 1000000007;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		treeL = getL(N);
		sIdx = treeL / 2 - 1;
		
		tree = new long[treeL];
		
		for (int i = 0; i < treeL; i++) {
			tree[i] = 1;
		}
		
		for (int i = sIdx+1; i <= sIdx + N; i++) {
			tree[i] = Long.parseLong(br.readLine());
		}
		
		treeSet(treeL-1);
		
		for (int mk = 0; mk < M + K; mk++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken()) + sIdx;
			if (a == 1) {
				long c = Long.parseLong(st.nextToken());
				updateTree(b, c);
//				printTree();
			}
			else {
				int c = Integer.parseInt(st.nextToken()) + sIdx;
				System.out.println(myAns(b, c));
			}
		}
		
//		printTree();
	}
	
	public static long myAns(int s, int e) {
		long ret = 1;
		while (s <= e) {
			if (s % 2 == 1) {
				ret = ret * tree[s] % myMod;
				s++;
			}
			if (e % 2 == 0) {
				ret = ret * tree[e] % myMod;
				e--;
			}
			s = s / 2;
			e = e / 2;
		}
		return ret;
	}
	
	public static void updateTree(int i, long num) {
		tree[i] = num % myMod;
		while (i != 1) {
			i /= 2;
			tree[i] = tree[i * 2] % myMod * tree[i * 2 + 1] % myMod;
		}
	}
	
	public static void treeSet(int n) {
		while (n != 1) {
			tree[n / 2] = tree[n / 2] * tree[n] % myMod;
			n--;
		}
	}
	
	public static int getL(int n) {
		int ret = 1;
		
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