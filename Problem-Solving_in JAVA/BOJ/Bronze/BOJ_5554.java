import java.io.*;
import java.util.*;


public class BOJ_5554 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int t = 0;
		
		for (int i = 0; i < 4; i++) {
			t += sc.nextInt();
		}
		
		System.out.println(t / 60);
		System.out.println(t % 60);

	}

}
