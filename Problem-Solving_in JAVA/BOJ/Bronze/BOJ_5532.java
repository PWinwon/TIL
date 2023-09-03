import java.io.*;
import java.util.*;


public class BOJ_5532 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int L = sc.nextInt();
		int A = sc.nextInt();
		int B = sc.nextInt();
		int C = sc.nextInt();
		int D = sc.nextInt();
		
		int korean = A / C;
		if (A % C > 0) korean++;
		
		int mHws = B / D;
		if (B % D > 0) mHws++;
		
		int maxHws = Math.max(korean, mHws);
		System.out.println(L - maxHws);

	}

}
