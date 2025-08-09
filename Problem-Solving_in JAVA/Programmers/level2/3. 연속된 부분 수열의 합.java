import java.util.*;

class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = new int[2];
        
        // 투포인터 활용
        // 초기 값 배열의 첫 원소
        // 시작 index s, 끝 index e
        // 값이 k보다 작으면 오른쪽으로 한칸 증가, 총 합 += 해당 칸 값
        // 값이 k보다 크면 왼쪽으로 한칸 증가, 총 합 -= 해당 칸 값
        int s = 0;
        int e = 0;
        int total = sequence[0];
        ArrayList<Point> list = new ArrayList<>();
        
        while (e < sequence.length && s < sequence.length) {
            if (total == k) {
                list.add(new Point(s, e));
                System.out.println("s : " + s + ", e : " + e);
            } 
            
            if (total <= k) {
                // e++ 해야하는데 범위 밖이면 break;
                e++;
                if (e < sequence.length) {
                    total += sequence[e];
                }
            } else {
                s++;
                if (s < sequence.length) {
                    total -= sequence[s];
                }
            }
        }

        Collections.sort(list);

        if (list.isEmpty()) {
            return answer;
        } else {
            
            Point a = list.get(0);

            answer[0] = a.s;
            answer[1] = a.e;
        }
        
        return answer;
    }
}


class Point implements Comparable<Point> {
    int s;
    int e;
    Point(int s, int e) {
        this.s = s;
        this.e = e;
    }
    
    @Override
    public int compareTo(Point o) {
        int tLen = this.e - this.s;
        int oLen = o.e - o.s;
        if (tLen < oLen) return -1;
        else if (tLen > oLen) return 1;
        return this.s - o.s;
    }    
}