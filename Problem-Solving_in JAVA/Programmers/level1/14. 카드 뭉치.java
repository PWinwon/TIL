class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "Yes";
        
        // 반복문을 순회하면서 각 카드를 확인해서 현재 목표 배열을 만들 수 있는지 확인.
        int idx1 = 0;
        int idx2 = 0;
        int idx = 0;
        
        while (idx < goal.length) {
            // 현재 카드 뭉치 1의 사용해야하는 카드가 목표 배열의 카드와 같은지
            if (idx1 < cards1.length && cards1[idx1].equals(goal[idx])) {
                idx1++;
                idx++;
            } else if (idx2 < cards2.length && cards2[idx2].equals(goal[idx])) {
                idx2++;
                idx++;
            } else {
                answer = "No";
                break;
            }
        }
        
        return answer;
    }
}