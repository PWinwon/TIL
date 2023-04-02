// Main
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution
{
	private final static int CMD_INIT       = 100;
	private final static int CMD_INSERT     = 200;
	private final static int CMD_MOVECURSOR = 300;
	private final static int CMD_COUNT      = 400;
	
	private final static UserSolution usersolution = new UserSolution();
	
	private static void String2Char(char[] buf, String str, int maxLen)
	{
		for (int k = 0; k < str.length(); k++)
			buf[k] = str.charAt(k);
			
		for (int k = str.length(); k <= maxLen; k++)
			buf[k] = '\0';
	}
	
	private static char[] mStr = new char[90001];
	
	private static boolean run(BufferedReader br) throws Exception
	{
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int queryCnt = Integer.parseInt(st.nextToken());
		boolean correct = false;
		
		for (int q = 0; q < queryCnt; q++)
		{
			st = new StringTokenizer(br.readLine(), " ");
			
			int cmd = Integer.parseInt(st.nextToken());
			
			if (cmd == CMD_INIT)
			{
				int H = Integer.parseInt(st.nextToken());
				int W = Integer.parseInt(st.nextToken());
				
				String2Char(mStr, st.nextToken(), 90000);
				
				usersolution.init(H, W, mStr);
				correct = true;
			}
			else if (cmd == CMD_INSERT)
			{
				char mChar = st.nextToken().charAt(0);
				
				usersolution.insert(mChar);
			}
			else if (cmd == CMD_MOVECURSOR)
			{
				int mRow = Integer.parseInt(st.nextToken());
				int mCol = Integer.parseInt(st.nextToken());
				
				char ret = usersolution.moveCursor(mRow, mCol);
				
				char ans = st.nextToken().charAt(0);
				if (ret != ans)
				{
					correct = false;
				}
			}
			else if (cmd == CMD_COUNT)
			{
				char mChar = st.nextToken().charAt(0);
				
				int ret = usersolution.countCharacter(mChar);
				
				int ans = Integer.parseInt(st.nextToken());
				if (ret != ans)
				{
					correct = false;
				}
			}
		}
		return correct;
	}

	public static void main(String[] args) throws Exception
	{
		int TC, MARK;
		
		int de = -1;
		
		System.setIn(new java.io.FileInputStream("src/res/sample_input.txt"));
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		TC = Integer.parseInt(st.nextToken());
		MARK = Integer.parseInt(st.nextToken());
		
		for (int testcase = 1; testcase <= TC; ++testcase)
		{
			int score = run(br) ? MARK : 0;
			
			System.out.println("#" + testcase + " " + score);
		}
		
		br.close();
	}
}


// UserSolution

import java.util.HashMap;

class UserSolution
{
	private StringBuffer sb;
	
	private int sbSize;
	
	private int hRow;
	private int wCol;
	
	private int curLocation;
	private int maxLength;
	
	
	void init(int H, int W, char mStr[])
	{
		int idx = 0;
		
		while (true) {
			if (mStr[idx] == '\0') {
				break;
			}
			idx++;
		}
		
		this.sb = new StringBuffer(new String(mStr).substring(0, idx));
		this.maxLength = this.sb.length();
		this.hRow = H;
		this.wCol = W;
		this.curLocation = 0;
	}
	
	void insert(char mChar)
	{
		this.sb.insert(this.curLocation, mChar);
		this.curLocation++;
		this.maxLength++;
	}

	char moveCursor(int mRow, int mCol)
	{
		this.curLocation = (mRow-1) * this.wCol + mCol - 1;
		if (this.curLocation >= this.maxLength) {
			this.curLocation = this.maxLength;
			return '$';
		}
		else {
			return this.sb.substring(this.curLocation, this.curLocation+1).toCharArray()[0];
		}
	}

	int countCharacter(char mChar)
	{
		if (this.curLocation >= this.maxLength) {			
			return 0;
		}
		int retCnt = 0;
		String str = this.sb.toString();
		int idx = str.indexOf(mChar, this.curLocation);
		
		while (idx != -1) {
			retCnt++;
			idx = str.indexOf(mChar, idx+1);
		}
		
		return retCnt;
	}
}