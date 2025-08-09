import java.util.*;

class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        
        // 칠해야하는 구역 오름차순 정렬
        Arrays.sort(section);
        // 현재 칠하는 구역 변수 now 선언
        int now = 0;
        
        for (int i = 0; i < section.length; i++) {
            // 현재 칠해야하는 구역이 now보다 크다면 칠하는 구역 갱신
            if (now < section[i]) {
                answer++;
                now = section[i] + m - 1;
            }
        }
        
        
        return answer;
    }
}