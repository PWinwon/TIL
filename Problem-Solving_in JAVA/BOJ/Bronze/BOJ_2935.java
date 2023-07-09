import java.io.*;
import java.util.*;
import java.math.BigInteger;


public class BOJ_2935 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		BigInteger A = new BigInteger(br.readLine());
		String s = br.readLine();
		BigInteger B = new BigInteger(br.readLine());
		
		
		if (s.equals("+")) System.out.println(A.add(B));
		else System.out.println(A.multiply(B));

	}

}
