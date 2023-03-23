import java.io.*;
import java.util.*;


public class BOJ_12891 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int S = Integer.parseInt(st.nextToken());
		int P = Integer.parseInt(st.nextToken());
		
		String s = br.readLine();
		char[] sArray = s.toCharArray();
		
		st = new StringTokenizer(br.readLine());
		int[] check = new int [4];
		
		for (int i = 0; i < 4; i++) {
			check[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] sWindow = new int [4];
		int idx = -1;
		for (int p = 0; p < P; p++) {
			idx = aCheck(sArray[p]);
			if (idx == -1) {
				continue;
			}
			sWindow[idx] += 1;
		}
		
		int sIdx = 0;
		int eIdx = P;
		int sRet = -1;
		int eRet = -1;
		boolean flag = true;
		
		int answer = 0;
		
		
		while (true) {
			flag = true;
			for (int i = 0; i < 4; i++) {
				if (check[i] <= sWindow[i]) {
					continue;
				}
				flag = false;
				break;
			}
			
			if (flag) {
				answer++;
			}
			
			if (eIdx == S) {
				break;
			}
			
			sRet = aCheck(sArray[sIdx]);
			eRet = aCheck(sArray[eIdx]);
			
			sWindow[sRet]--;
			sWindow[eRet]++;
			
			sIdx++;
			eIdx++;
			
		}
		
		System.out.print(answer);
		
	}
	
	public static int aCheck(char a) {
		switch (a) {
			case 'A' : 
				return 0;
		case 'C' :
			return 1;
		case 'G' :
			return 2;
		case 'T' :
			return 3;
		default :
			return -1;
		}
	}

}
