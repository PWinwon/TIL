import java.io.*;
import java.util.*;


public class BOJ_11478 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str = br.readLine();
		HashSet<String> mySet = new HashSet<String>();		
		
		for (int s = 0; s < str.length(); s++) {
			for (int e = s+1; e < str.length()+1; e++) {
				mySet.add(str.substring(s, e));
//				System.out.println(str.substring(s, e));
			}
		}
		
//		for (int i = 0; i < mySet.size()-1; i++) {
//			System.out.println
//		}
//		
		System.out.println(mySet.size());

	}

}
