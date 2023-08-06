import java.io.*;
import java.util.*;


public class BOJ_2083 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		while (true) {
			st = new StringTokenizer(br.readLine());
			String name = st.nextToken();
			int age = Integer.parseInt(st.nextToken());
			int weight = Integer.parseInt(st.nextToken());
			
			if (name.equals("#") && age == 0 && weight == 0) break;
			else if (age > 17 || weight >= 80) {
				System.out.println(name + " Senior");
			}
			else System.out.println(name + " Junior");
		}

	}

}
