import java.util.*;

public class QueueStack {
    Queue<Integer> q1 = new LinkedList<>();
    Queue<Integer> q2 = new LinkedList<>();

    public void push(int x) {
        q1.add(x);
    }

    public int pop() {
        if (q1.isEmpty()) return -1;

        while (q1.size() > 1)
            q2.add(q1.remove());

        int val = q1.remove();

        Queue<Integer> temp = q1;
        q1 = q2;
        q2 = temp;

        return val;
    }
}
