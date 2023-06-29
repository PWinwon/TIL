import java.io.*;
import java.util.*;


public class BOJ_10953 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		for (int i = 0; i < N; i++) {
			String[] strs = sc.next().split(",");
//			System.out.println(strs[0]);
			int a = Integer.parseInt(strs[0]);
			int b = Integer.parseInt(strs[1]);
			System.out.println(a+b);
		}

	}

}
