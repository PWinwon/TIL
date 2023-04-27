import java.io.*;
import java.util.*;


public class Swea_3 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
//		Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = 10;
		LinkedList<String> pwd;
		
		for (int tc = 1; tc < T+1; tc++) {
			int N = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			
			pwd = new LinkedList<>();
			
			for (int i = 0; i < N; i++) {
				pwd.add(st.nextToken());
			}
			
			int M = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine(), " ");
			int x;
			int y;
			for (int m = 0; m < M; m++) {
				switch (st.nextToken()) {
				case "I":
					x = Integer.parseInt(st.nextToken());
					y = Integer.parseInt(st.nextToken());
					
					for (int i = 0; i < y; i++) {
						pwd.add(x++, st.nextToken());
//						x++;
					}
					break;
					
				case "D":
					x = Integer.parseInt(st.nextToken());
					y = Integer.parseInt(st.nextToken());
					
					for (int i = 0; i < y; i++) {
						pwd.remove(x);
					}
					break;
					
				case "A":
					y = Integer.parseInt(st.nextToken());
					
					for (int i = 0; i < y; i++) {
						pwd.add(st.nextToken());
					}
					break;
				}
			}
			
			sb.append("#").append(tc).append(" ");
			
			for (int i = 0; i < 10; i++) {
				sb.append(pwd.get(i)).append(" ");
			}
			
			sb.append("\n");
		}
		System.out.println(sb);
	}

}
