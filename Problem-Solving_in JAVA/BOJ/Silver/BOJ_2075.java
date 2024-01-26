import java.io.*;
import java.util.*;


public class BOJ_2304 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		int[][] myMap = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				myMap[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		int[] idxs = new int[N];
		
		int n = 0;
		PriorityQueue<Number> pq = new PriorityQueue<>();
		
		for (int i = 0; i < N; i++) {
			pq.add(new Number(myMap[N-1][i], i, N-1));
		}
		
		int result = -1;
		
		while (n < N) {
			// n번째 숫자빼기
			Number num = pq.poll();
			result = num.val;
			// 숫자 하나 채우기
			n++;
			if (num.lev-1 < 0) continue;
			pq.add(new Number(myMap[num.lev-1][num.idx], num.idx, num.lev-1));
		}
		
		System.out.println(result);

	}

}


class Number implements Comparable<Number>{
	int val;
	int idx;
	int lev;
	
	Number(int v, int i, int l) {
		this.val = v;
		this.idx = i;
		this.lev = l;
	}
	@Override
	public int compareTo(Number o) {
		return o.val - this.val;
		
	}
}