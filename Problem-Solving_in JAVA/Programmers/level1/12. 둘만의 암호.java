import java.io.*;
import java.util.*;

class Solution {
    public String solution(String s, String skip, int index) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        
        // 스킵을 제외한 알파벳 배열 만들기
        // 배열을 하면 나중에 찾을때 비효율적인거같음. 
        // HashMap 2개 만들어서 서로 찾을까?
        // 문자로 현재 index 찾고, index에 필요한만큼 더해서 새로운 char 찾기
        char[] skipArr = skip.toCharArray();
        
        HashMap<Character, Integer> charToInt = new HashMap<>();
        HashMap<Integer, Character> intToChar = new HashMap<>();
        
        int idx = 0;
        
        for (int i = 0; i < 26; i++) {
            char c = (char) ('a' + i);
            boolean flag = true;
            for (int j = 0; j < skipArr.length; j++) {
                if (c == skipArr[j]) {
                    flag = false;
                    break;
                }
            }
            
            if (flag) {
                charToInt.put(c, idx);
                intToChar.put(idx, c);
                idx++;
            }
        }
        
        // s 를 순회하며 생성된 alpha의 skip 위치에 맞춰 새로운 문자열 sb 생성
        for (int i = 0; i < s.length(); i++) {
            char now = s.charAt(i);
            // 해당 문자의 스킵을 포함한 암호 해독문자 구하기
            int next = (charToInt.get(now) + index) % idx;
            sb.append(intToChar.get(next));
        }
        
        return sb.toString();
    }
}