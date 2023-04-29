import java.io.*;
import java.util.*;


public class BOJ_25206 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		double total = 0;
		double score = 0;
		double answer;
		
		for (int i = 0; i < 20; i++) {
			double temp = 0;
			
			st = new StringTokenizer(br.readLine(), " ");
			String subject = st.nextToken();
			double num = Float.parseFloat(st.nextToken());
			char[] grade = st.nextToken().toCharArray(); 
			
			if (grade[0] == 'P') {
				continue;
			}
			
			
			total += num;
			if (grade[0] == 'F') {
				continue;
			}
			
			temp = 4 - (grade[0] - 'A');
			if (grade[1] == '+') temp += 0.5;
			
			score += (temp * num);
		}
		
		answer = score / total;
		System.out.println(answer);
		
	}

}
