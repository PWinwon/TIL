import java.io.*;
import java.util.*;


public class BOJ_27433 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		System.out.println(getAns(N));

	}
	
	public static long getAns(int n) {
		long ret = 1;
		
		while (n != 0) {
			ret *= n;
			n--;
		}
		
		return ret;
	}

}
