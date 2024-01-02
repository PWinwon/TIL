import java.io.*;
import java.util.*;

public class Main {
	static int R, C;
	static int[] heights, heightMax;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		
		heights = new int[C];
		heightMax = new int[C];
		
		int leftMax = -1;
		int rightMax = -1;
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < C; i++) {
			heights[i] = Integer.parseInt(st.nextToken());
			heightMax[i] = Integer.MAX_VALUE;		
		}
		
		for (int i = 0; i < C; i++) {
			if (leftMax < heights[i]) {
				leftMax = heights[i];
			}
			heightMax[i] = Math.min(heightMax[i], leftMax);
			if (rightMax < heights[C - i - 1]) {
				rightMax = heights[C - i - 1];
			}
			heightMax[C - i - 1] = Math.min(heightMax[C - i - 1], rightMax);
		}
		
		int result = 0;
		
		for (int i = 0; i < C; i++) {
			if (heightMax[i] - heights[i] > 0) {
				result += heightMax[i] - heights[i];
			}
		}
		
		System.out.println(result);

	}

}
