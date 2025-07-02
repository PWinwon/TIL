class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        
        while (a <= n) {
            int addCola = (n / a) * b;
            n = n % a + addCola;
            
            answer += addCola;
        }
        
        
        return answer;
    }
}