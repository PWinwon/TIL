import java.util.*;
import java.io.*;


public class BOJ_2744 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String str = sc.next();
		char[] c = str.toCharArray();
		
		for (int i = 0; i < c.length; i++) {
			if (Character.isUpperCase(c[i])) {
				System.out.print(String.valueOf(c[i]).toLowerCase());
			}
			else {
				System.out.print(String.valueOf(c[i]).toUpperCase());
			}
		}

	}

}
