import java.util.*;
import java.io.*;


public class Main
{
    static boolean[] alphaChk = new boolean[26];
    static char[][] puzzle = new char[5][5];

    static int[] dr = {-1, 1};
    static int[] dc = {-1, 1};


    public static void main(String args[]) throws Exception
    {
        // J는 없앤다
        alphaChk[(int)'J' - 'A'] = true;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] str = br.readLine().toCharArray();
        // 2글자씩 나누기 전에 sb에 재구성하기
        StringBuilder sb = new StringBuilder();
        
        int idx = 0;

        while (idx < str.length) {
            // 남은 char가 2개이상인지
            if (idx+1 < str.length) {
                // str[idx] == str[idx+1] 같다면
                // idx++로 마무리
                if (str[idx] == str[idx+1]) {
                    // 같을때는 'X' 일 경우 + 마지막 남은 글자가 아닌 경우 => 이미 위에서 2개 이상인지 확인 했으므로, 마지막 글자가 아님이 보장
                    // idx+1 자리에는 'Q' 추가
                    if (str[idx] == 'X' ) {
                        sb.append(str[idx]).append('Q');
                    }
                    // 나머지는 'X' 추가
                    else {
                        sb.append(str[idx]).append('X');
                    }
                    idx++;
                }
                // 다르다면
                else {
                    sb.append(str[idx]).append(str[idx+1]);
                    idx += 2;
                }
            }
            // 하나 남았을때
            else {
                // 'X'인지 아닌지 확인 안해두댐
                sb.append(str[idx]).append('X');
                idx++;
            }
        }
        // 5*5 암호키바탕 배열 채우기
        // makePrimKey(br.readLine().toCharArray());
        char[] myKey = br.readLine().toCharArray();

        makePrimKey(myKey);

        // for (int i = 0; i < 5; i++) {
        //     for (int j = 0; j < 5; j++) {
        //         System.out.print(puzzle[i][j] + " ");
        //     }
        //     System.out.println();
        // }



        //step1. 2글자씩 규칙에 맞게 나누기
        char[] newStr = sb.toString().toCharArray();

        // for (int i = 0; i < newStr.length; i++) {
        //     System.out.print(newStr[i] + " ");
        // }

        for (int i = 0; i < newStr.length; i += 2) {
            char a = newStr[i];
            char b = newStr[i+1];
            Point pa = myFind(a);
            Point pb = myFind(b);
            // 1. 같은 행에 있는 경우 (y가 같은 경우)
            if (pa.y == pb.y) {
                newStr[i] = puzzle[pa.y][(pa.x+1)%5];
                newStr[i+1] = puzzle[pb.y][(pb.x+1)%5];
            }
            // 2. 같은 열에 있는 경우 (x가 같은 경우)
            else if (pa.x == pb.x) {
                newStr[i] = puzzle[(pa.y+1)%5][pa.x];
                newStr[i+1] = puzzle[(pb.y+1)%5][pb.x];
            }
            // 3. 둘다 아닌 경우
            else {
                newStr[i] = puzzle[pa.y][pb.x];
                newStr[i+1] = puzzle[pb.y][pa.x];
            }
        }

        for (int i = 0; i < newStr.length; i++) {
            System.out.print(newStr[i]);
        }
    }

    public static Point myFind(char x) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (puzzle[i][j] == x) return new Point(j, i);
            }
        }
        return new Point(-1, -1);
    }

    static class Point {
        int x;
        int y;
        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void makePrimKey(char[] str) {

        
        // for (int i = 0; i < str.length; i++) {
        //     System.out.print(str[i] + " ");
        // }
        int idx = 0;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                // 기존에 들어갔는지 체크
                while ((idx < str.length) && alphaChk[str[idx] - 'A']) {
                    idx++;
                }
                // 이미 str로 다 채웠는지 체크
                if (idx < str.length) {
                    puzzle[i][j] = str[idx];
                    alphaChk[str[idx] - 'A'] = true;
                }
                else {
                    for (int k = 0; k < 26; k++) {
                        if (alphaChk[k]) continue;
                        puzzle[i][j] = (char) (k + 'A');
                        alphaChk[k] = true;
                        break;
                    }
                }
            }
        }
    }
}