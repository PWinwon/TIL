import java.io.*;
import java.util.*;

public class BOJ_2357 {
	static int N, M, treeL, sIdx;
	static long[] maxTree;
	static long[] minTree;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		treeL = getL(N);
		sIdx = treeL / 2 - 1;
		
		maxTree = new long[treeL];
		minTree = new long[treeL];
		
		for (int i = 0; i < treeL; i++) {
			maxTree[i] = 0;
			minTree[i] = Long.MAX_VALUE;
		}
		
		for (int i = sIdx+1; i <= sIdx+N; i++) {
			long a = Long.parseLong(br.readLine());
			maxTree[i] = a;
			minTree[i] = a;
		}
		
		setTree(treeL-1);
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken()) + sIdx;
			int e = Integer.parseInt(st.nextToken()) + sIdx;
			myData ans = getAns(s, e);
			System.out.println(ans.minVal + " " + ans.maxVal);
		}
		
//		printTree();

	}
	
	public static myData getAns(int s, int e) {
		myData ret = new myData(-1, -1);
		long maxA = 0;
		long minA = Long.MAX_VALUE;
		
		while (s <= e) {
			if (s % 2 == 1) {
				minA = Math.min(minA, minTree[s]);
				maxA = Math.max(maxA, maxTree[s]);
				s++;
			}
			if (e % 2 == 0) {
				minA = Math.min(minA, minTree[e]);
				maxA = Math.max(maxA, maxTree[e]);
				e--;
			}
			s /= 2;
			e /= 2;
		}
		
		ret.maxVal = maxA;
		ret.minVal = minA;
		
		return ret;
	}
	
	
	public static void setTree(int n) {
		while (n != 1) {
			if (maxTree[n / 2] < maxTree[n]) maxTree[n / 2] = maxTree[n];
			if (minTree[n / 2] > minTree[n]) minTree[n / 2] = minTree[n];
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
			System.out.print(minTree[i] + " ");
		}
		
		System.out.println();
		
		for (int i = 0; i < treeL; i++) {
			System.out.print(maxTree[i] + " ");
		}
		
		System.out.println();
	}

}

class myData {
	long maxVal;
	long minVal;
	myData (long maxV, long minV) {
		this.maxVal = maxV;
		this.minVal = minV;
	}
}
