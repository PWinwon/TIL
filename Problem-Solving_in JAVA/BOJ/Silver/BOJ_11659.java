import java.io.*;
import java.util.*;

public class BOJ_11659 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
		
		
		int N = Integer.parseInt(stringTokenizer.nextToken());
		int M = Integer.parseInt(stringTokenizer.nextToken());
		
		long sumArray[] = new long[N+1];
		
		stringTokenizer = new StringTokenizer(bufferedReader.readLine());
		
		for (int i = 1; i < N+1; i++) {
			sumArray[i] = sumArray[i-1] + Integer.parseInt(stringTokenizer.nextToken());
		}
		
		for (int m = 0; m < M; m++) {
			stringTokenizer = new StringTokenizer(bufferedReader.readLine());
			int s = Integer.parseInt(stringTokenizer.nextToken());
			int e = Integer.parseInt(stringTokenizer.nextToken());
			bufferedWriter.write((sumArray[e] - sumArray[s-1]) + "\n");
			
		}
		bufferedWriter.close();

	}

}
