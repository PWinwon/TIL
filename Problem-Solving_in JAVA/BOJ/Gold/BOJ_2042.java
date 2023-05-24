import java.io.*;
import java.util.*;


public class BOJ_2042 {
	static int N, M, K, lenN, sIdx;
	
	static long[] tree;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		lenN = arrCnt(N);
		sIdx = lenN / 2 - 1;
		
		tree = new long[lenN];
		
		for (int i = lenN / 2; i < lenN / 2 + N; i++) {
			tree[i] = Long.parseLong(br.readLine());
		}
		
		makeTree(lenN-1);
		
//		printTree();
		
		for (int i = 0; i < M+K; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			long c = Long.parseLong(st.nextToken());
			
			if (a == 1) {
				updateTree(b + sIdx, c);
//				printTree();
			}
			else {
				b += sIdx;
				c += sIdx;
				System.out.println(mySum(b, (int) c));
			}
		}

	}
	
	public static long mySum(int s, int e) {
		long ret = 0;
		while (s <= e) {
			if (s % 2 == 1) {
				ret += tree[s];
				s++;
			}
			if (e % 2 == 0) {
				ret += tree[e];
				e--;
			}
			s = s / 2;
			e = e / 2;
		}
		return ret;
	}
	
	public static void updateTree(int n, long val) {
		long diff = val - tree[n];
		
		while (n > 0) {
			tree[n] += diff;
			n /= 2;
		}
	}
	
//	public static void printTree() {
//		for (int i = 0; i < lenN; i++) {
//			System.out.print(tree[i] + " ");
//		}
//		System.out.println();
//	}
	
	public static void makeTree(int n) {
		while (n != 1) {
			tree[n / 2] += tree[n];
			n--;
		}
	}
	
	public static int arrCnt(int n) {
		int ret = 1;
		while (ret < n) {
			ret *= 2;
		}
		return ret * 2;
	}

}
