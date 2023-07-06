import java.io.*;
import java.util.*;


public class BOJ_10824 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		String A = st.nextToken() + st.nextToken();
		String B = st.nextToken() + st.nextToken();
		
		long a = Long.parseLong(A);
		long b = Long.parseLong(B);
		
		System.out.println(a+b);

	}

}
