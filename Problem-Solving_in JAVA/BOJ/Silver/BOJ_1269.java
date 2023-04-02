import java.io.*;
import java.util.*;


public class BOJ_1269 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int sA = Integer.parseInt(st.nextToken());
		int sB = Integer.parseInt(st.nextToken());
		
		int[] A = new int [sA];
		int[] B = new int [sB];
		
		TreeSet<Integer> treeA = new TreeSet<>();
		TreeSet<Integer> treeB = new TreeSet<>();
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < sA; i++) {
			int a = Integer.parseInt(st.nextToken());
			treeA.add(a);
			A[i] = a;
		}
		
		st = new StringTokenizer(br.readLine());
		
		for (int j = 0; j < sB; j++) {
			int b = Integer.parseInt(st.nextToken());
			treeB.add(b);
			B[j] = b;
		}
		
		for (int i : B) {
			treeA.remove(i);
		}
		
		for (int j : A) {
			treeB.remove(j);
		}
		
		System.out.println(treeA.size() + treeB.size());
	}

}
