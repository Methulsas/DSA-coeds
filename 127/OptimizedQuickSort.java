//  OptimizedQuickSort.java

class OptimizedQuickSort {


// Main method to test Quick Sort
public static void main(String[] args) {
int[] arr = {10, 7, 8, 9, 1, 5};


System.out.println("Before Sorting:");
for (int x : arr) System.out.print(x + " ");


quickSort(arr, 0, arr.length - 1);


System.out.println("\nAfter Sorting:");
for (int x : arr) System.out.print(x + " ");
}


// Quick Sort function
public static void quickSort(int[] arr, int low, int high) {
if (low < high) {
int pi = partition(arr, low, high); // pivot index
quickSort(arr, low, pi - 1); // left side
quickSort(arr, pi + 1, high); // right side
}
}


// Partition logic
private static int partition(int[] arr, int low, int high) {
int pivot = arr[high]; // last element as pivot
int i = low - 1;


for (int j = low; j < high; j++) {
if (arr[j] <= pivot) {
i++;
int temp = arr[i];
arr[i] = arr[j];
arr[j] = temp;
}
}


int temp = arr[i + 1];
arr[i + 1] = arr[high];
arr[high] = temp;


return i + 1;
}
}