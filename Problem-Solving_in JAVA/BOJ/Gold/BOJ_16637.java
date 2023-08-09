import java.io.*;
import java.util.*;


public class BOJ_16637 {
	
	static ArrayList<Character> oper;
	static ArrayList<Integer> num;
	
	static int answer;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		char[] exp = br.readLine().toCharArray();
		
		oper = new ArrayList<Character>();
		num = new ArrayList<Integer>();
		
		for (int i = 0; i < N; i++) {
			if (exp[i] - '0' < 10 && exp[i] - '0' >= 0) num.add(exp[i] - '0');
			else oper.add(exp[i]);
		}
		
		answer = Integer.MIN_VALUE;
		
		myFunc(num.get(0), 0);
		
		System.out.println(answer);

	}
	
	public static void myFunc(int total, int idx) {
		if (idx >= oper.size()) {
			answer = Math.max(total, answer);
			return;
		}
		
		myFunc(calc(oper.get(idx), total, num.get(idx+1)), idx+1);
		
		if (idx + 1 < oper.size()) {
			myFunc(calc(oper.get(idx), total, calc(oper.get(idx+1), num.get(idx+1), num.get(idx+2))), idx+2);
		}
		return;
	}
	
	public static int calc(char o, int a, int b) {
		switch (o) {
			case '+':
				return a + b;
			case '-':
				return a - b;
			default:
				return a * b;
		}
	}

}
