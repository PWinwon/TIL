import java.io.*;
import java.util.*;


public class BOJ_2750 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int[] lst = new int [N];
		
		for (int n = 0; n < N; n++) {
			lst[n] = Integer.parseInt(br.readLine());
		}
		
		int temp = -1;
		
		for (int i = 0; i < N-1; i++) {
			for (int j = i+1; j < N; j++) {
				if (lst[i] > lst[j]) {
					temp = lst[i];
					lst[i] = lst[j];
					lst[j] = temp;
				}
			}
		}
		
		for (int i = 0; i < N; i++) {
			System.out.println(lst[i]);
		}
	}

}
