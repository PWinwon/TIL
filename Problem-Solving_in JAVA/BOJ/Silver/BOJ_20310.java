import java.io.*;
import java.util.*;


public class BOJ_20310 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuffer sb = new StringBuffer();
		
		int zCnt = 0;
		int oCnt = 0;
		char[] temp = br.readLine().toCharArray();
		
		for (int i = 0; i < temp.length; i++) {
			if (temp[i] == '0') zCnt++;
			else oCnt++;
		}
		
		zCnt /= 2;
		oCnt /= 2;
		
		for (int i = 0; i < temp.length; i++) {
			//이면서 zCnt > 0 이면 추가
			if (temp[i] == '0' && zCnt > 0) {
				sb.append(temp[i]);
				zCnt--;
			}
			else if (temp[i] == '1') {
				if (oCnt > 0) {
					oCnt--;
				}
				else {
					sb.append(temp[i]);
				}
			}
		}
		
		System.out.println(sb);
		

	}

}
