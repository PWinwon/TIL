import java.io.*;
import java.util.*;


public class BOJ_2440 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		StringBuffer sb = new StringBuffer();
		
		int N = sc.nextInt();
		
		for (int i = N; i > 0; i--) {
			for (int j = 0; j < i; j++) {
				sb.append("*");
			}
			sb.append("\n");		
		}
		
		System.out.println(sb);

	}

}
