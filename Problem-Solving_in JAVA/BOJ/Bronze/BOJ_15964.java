import java.io.*;
import java.util.*;

public class BOJ_15964 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		System.out.println(myFunc(a, b));

	}
	
	public static long myFunc(int a, int b) {
		long plus = a + b;
		long minus = a - b;
		
		return plus * minus;
	}

}
