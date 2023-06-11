import java.io.*;
import java.util.*;


public class BOJ_2754 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		char[] c = s.toCharArray();
		boolean flag = true;
		
		float ret = 0f;
		switch (c[0]) {
			case 'A':
				ret += 4;
				break;
			case 'B':
				ret += 3;
				break;
			case 'C':
				ret += 2;
				break;
			case 'D':
				ret += 1;
				break;
			default:
				flag = false;
				break;
		}
		
		if (flag) ret += myOper(c[1]);
		
		System.out.println(ret);

	}
	
	public static float myOper(char a) {
		if (a == '+') return 0.3f;
		else if (a == '-') return -0.3f;
		return 0f;
	}

}
