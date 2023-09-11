import java.io.*;
import java.util.*;


public class BOJ_10039 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int total = 0;
		
		for (int i = 0; i < 5; i++) {
			int a = sc.nextInt();
			if (a < 40) a = 40;
			total += a;
		}
		
		System.out.println(total / 5);

	}

}
