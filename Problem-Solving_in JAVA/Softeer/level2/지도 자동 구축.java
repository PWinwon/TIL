import java.util.*;
import java.io.*;


public class Main
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] dp = new int[n+1];

        dp[0] = 2;

        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-1] - 1;
        }

        System.out.println((int) Math.pow(dp[n], 2));
    }

}