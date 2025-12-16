public class UnboundedArrayStack {
    private int[] arr = new int[2];
    private int top = -1;

    public void push(int x) {
        if (top == arr.length - 1) {
            int[] newArr = new int[arr.length * 2];
            System.arraycopy(arr, 0, newArr, 0, arr.length);
            arr = newArr;
        }
        arr[++top] = x;
    }

    public int pop() {
        if (top == -1) return -1;

        int val = arr[top--];

        if (top > 0 && top == arr.length / 4) {
            int[] newArr = new int[arr.length / 2];
            System.arraycopy(arr, 0, newArr, 0, top + 1);
            arr = newArr;
        }
        return val;
    }
}
