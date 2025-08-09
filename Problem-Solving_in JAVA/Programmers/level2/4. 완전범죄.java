import java.util.*;


class Solution {
    
    static int N, answer, limitA, limitB;
    static int[][] infos;
    static HashSet<String> visited;
    
    public int solution(int[][] info, int n, int m) {

        answer = 121;
        limitA = n;
        limitB = m;
        N = info.length;
        visited = new HashSet<>();
        
        infos = new int[info.length][2];
        
        for (int i = 0; i < info.length; i++) {
            for (int j = 0; j < 2; j++) {
                infos[i][j] = info[i][j];
            }
        }
        
        dfs(0, 0, 0);
        
        if (answer > 120) answer = -1;
        
        return answer;
    }
    
    public void dfs(int n, int a, int b) {
        if (n == N) {
            if (a < answer) answer = a;
            return;
        }
        
        // 현재 상태 저장
        // 해당 상태와 동일한 상태가 입력될 경우 중복 탐색 방지
        String key = a + "," + b + "," + n;
        if (visited.contains(key)) {
            return;
        }
        
        // 현재 물건 A가 훔친경우
        if (a+infos[n][0] < limitA) {
            dfs(n+1, a+infos[n][0], b);
        }
        
        // 현재 물건 B가 훔친경우
        if (b+infos[n][1] < limitB) {
            dfs(n+1, a, b+infos[n][1]);
        }
        
        visited.add(key);
        
        return;
    }
}