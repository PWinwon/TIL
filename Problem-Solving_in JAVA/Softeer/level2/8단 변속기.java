import java.util.*;
import java.io.*;


public class Main
{
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        boolean isAsc = true;
        boolean isMix = false;

        int num = -1;
        int calc = 0;

        int a = Integer.parseInt(st.nextToken());
        switch (a) {
            case 1: {
                num = 2;
                calc = 1;
                break;
            }
            case 8: {
                isAsc = false;
                num = 7;
                calc = -1;
                break;
            }
            default: {
                isMix = true;
                break;
            }
        }

        for (int i = 0; i < 7; i++) {
            if (num == Integer.parseInt(st.nextToken())) num += calc;
            else {
                isMix = true;
                break;
            }
        }

        if (isMix) System.out.println("mixed");
        else if (isAsc) System.out.println("ascending");
        else System.out.println("descending");

    }
}