import java.io.*;
import java.math.BigInteger;
import java.util.*;


public class BOJ_1271 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		StringTokenizer st = new StringTokenizer(br.readLine());
		
		Scanner sc = new Scanner(System.in);
		
//		int A = Integer.parseInt(st.nextToken());
//		int B = Integer.parseInt(st.nextToken());
		
		BigInteger A = sc.nextBigInteger();
		BigInteger B = sc.nextBigInteger();
		
		System.out.println(A.divide(B));
		System.out.println(A.mod(B));

	}

}
