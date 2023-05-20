import java.util.*;
import java.io.*;


public class Main
{
    static int[] numLED = {119, 36, 93, 109, 46, 107, 123, 39, 127, 111, 0};
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < T; tc++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            System.out.println(myFunc(a, b));
        }
    }

    static public int myFunc(int a, int b) {
        int ret = 0;

        for (int i = 0; i < 5; i++) {
            int modA = a % 10;
            int modB = b % 10;
            if (a == 0) modA = 10;
            if (b == 0) modB = 10;
            ret += cntLED(numLED[modA], numLED[modB]);
            a /= 10;
            b /= 10;
        }
        return ret;
    }

    static public int cntLED(int a, int b) {
        int ret = 0;
        // System.out.println(a);
        // System.out.println(b);
        
        int num = a ^ b;
        // System.out.println(num);

        for (int i = 0; i < 7; i++) {
            if ((num & (1 << i)) > 0) ret++;
        }
        // System.out.println(ret);
        // System.out.println("-----------------------------------");
        return ret;
    }
}