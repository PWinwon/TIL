import java.util.*;

class Solution {
    public String[] solution(String[][] plans) {
        String[] answer = new String[plans.length];
        // 배열이 시간순으로 정렬되어있지않음. >> 정렬을 먼저해야함.
        Plan[] planArr = new Plan[plans.length];
        
        // 시작 시간은 모두 분으로 바꿔서 순서를 정립할 수 있도록 변형함.
        for (int i = 0; i < plans.length; i++) {
            String[] now = plans[i];
            String[] sTime = now[1].split(":");
            int startTime = Integer.parseInt(sTime[0]) * 60 + Integer.parseInt(sTime[1]);
            planArr[i] = new Plan(now[0], startTime, Integer.parseInt(now[2]));
        }
        
        Arrays.sort(planArr);
        
        // 정렬된 배열을 순회하며 과제를 진행
        // 작업을 진행할 stck 생성
        Stack<Plan> stck = new Stack<>();
        int nowTime = 0;
        int aIdx = 0;
        // stck에 작업이 남아있으면 계속 진행.
        // 현재 stck의 작업중인 과제는 가장 앞에 저장됨.
        
        for (int i = 0; i < planArr.length; i++) {
            Plan now = planArr[i];
            
            // 현재 stck에 작업이 있는데, 해당 작업이 지금 작업 시작전에 해결가능하다면
            // 해결 가능한지 확인하는 방법은 현재 시간 + 현재 과제 걸리는 남은 시간 <= 새로운 과제 시작 시간
            // System.out.println("nowTime : " + nowTime);
            while (!stck.isEmpty() && nowTime + stck.peek().time <= now.start) {
                Plan temp = stck.pop();
                nowTime += temp.time;
                answer[aIdx] = temp.subject;
                aIdx++;
            }
            
            // stck가 비어있으면 현재 작업 추가 및 nowTime 최신화
            if (stck.isEmpty()) {
                stck.push(now);
                nowTime = now.start;
            } else {
                // 비어있지 않다면 남은시간에 stck의 최상단에 남아있는 과제를 진행해야함
                // 진행되는 시간은 다음 과제 시작 시간 - 현재 시간만큼 과제를 진행함으로 해당 값을 빼주어야함.
                stck.peek().time -= now.start - nowTime;
                // System.out.println("now : " + stck.peek().subject + ", " + stck.peek().time);
                
                // 그리고 현재 과제가 stck에 들어감
                stck.push(now);
                nowTime = now.start;
            }
        }
        
        while(!stck.isEmpty()) {
            Plan now = stck.pop();
            answer[aIdx] = now.subject;
            aIdx++;
        }
        
        return answer;
    }
}


class Plan implements Comparable<Plan> {
    String subject;
    int start;
    int time;
    
    Plan(String s, int start, int t) {
        this.subject = s;
        this.start = start;
        this.time = t;
    }
    
    @Override
    public int compareTo(Plan o) {
        return this.start - o.start;
    }
}