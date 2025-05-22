import java.util.*;


class Solution {
    
    static int fCnt;
    static int[] points;
    static int[][] forYou;
    static HashMap<String, Person> persons;
    
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        
        fCnt = friends.length;
        points = new int[fCnt];
        forYou = new int[fCnt][fCnt];
        persons = new HashMap<>();
        
        // 2차원 배열에다가 선물 준 횟수 입력
        for (int i = 0; i < fCnt; i++) {
            persons.put(friends[i], new Person(i));
        }
        // HashMap에 선물 지수 저장
        for (int i = 0; i < gifts.length; i++) {
            String[] now = gifts[i].split(" ");
            Person a = persons.get(now[0]);
            Person b = persons.get(now[1]);
            
            forYou[a.idx][b.idx]++;
            forYou[b.idx][a.idx]--;
            
            points[a.idx]++;
            points[b.idx]--;
        }
        
        for (int i = 0; i < fCnt; i++) {
            int ret = 0;
            for (int j = 0; j < fCnt; j++) {
                // i랑 j를 비교
                if (i == j) continue;
                if (forYou[i][j] > 0 || (forYou[i][j] == 0 && points[i] > points[j])) {
                    ret++;
                }
            }
            
            if (answer < ret) answer = ret;
        }
        
        
        return answer;
    }
}


class Person {
    int idx;
    
    Person(int i) {
        this.idx = i;
    }
}