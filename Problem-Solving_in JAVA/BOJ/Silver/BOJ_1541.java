import java.io.*;
import java.util.*;


public class BOJ_1541 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str = br.readLine();
		
		String[] strArray = str.split("-");
		
		int answer = strSum(strArray[0]);
		
		for (int i = 1; i < strArray.length; i++) {
			answer -= strSum(strArray[i]);
		}
		
		System.out.println(answer);
	}

	public static int strSum(String s) {
		String[] temp = s.split("[+]");
		
		int ret = 0;
		
		for (int i = 0; i < temp.length; i++) {
			ret += Integer.parseInt(temp[i]);
		}
		
		return ret;
	}
}
