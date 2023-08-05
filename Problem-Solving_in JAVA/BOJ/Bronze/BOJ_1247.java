import java.io.*;
import java.util.*;
import java.math.*;


public class BOJ_1247 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for (int i = 0; i < 3; i++) {
			int N = Integer.parseInt(br.readLine());
			
			BigInteger S = new BigInteger("0");
			
			for (int j = 0; j < N; j++) {
				BigInteger N2 = new BigInteger(br.readLine());
				S = S.add(N2);
			}
			
			if (S.compareTo(BigInteger.ZERO) == -1) {
				System.out.println("-");
			}
			else if (S.compareTo(BigInteger.ZERO) == 1) {
				System.out.println("+");
			}
			else System.out.println(0);
		}

	}

}
