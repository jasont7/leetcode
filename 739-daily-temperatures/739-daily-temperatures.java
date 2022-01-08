import java.util.*;

class Solution {
    public int[] dailyTemperatures(int[] T) {
        int[] A = new int[T.length];
        Stack<Integer> stack = new Stack<>();
        for (int i=0; i < T.length; i++) {
            if (stack.isEmpty()) {
                stack.push(i);
            } else if (T[i] <= T[stack.peek()]) {
                stack.push(i);
            } else {
                while (T[i] > T[stack.peek()]) {
                    A[stack.peek()] = i - stack.pop();

                    if (stack.isEmpty()) break;
                }
                stack.push(i);
            }
        }
        while (!stack.isEmpty())
            A[stack.pop()] = 0;

        return A;
    }
}