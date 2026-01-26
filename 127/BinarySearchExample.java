// FILE 2: BinarySearchExample.java

class BinarySearchExample {


// Main method
public static void main(String[] args) {
int[] arr = {2, 4, 6, 8, 10, 12, 14}; // sorted array
int key = 10;


int result = binarySearch(arr, key);


if (result == -1)
System.out.println("Element not found");
else
System.out.println("Element found at index: " + result);
}


// Binary Search method
public static int binarySearch(int[] arr, int key) {
int low = 0;
int high = arr.length - 1;


while (low <= high) {
int mid = low + (high - low) / 2;


if (arr[mid] == key)
return mid;


if (arr[mid] < key)
low = mid + 1;
else
high = mid - 1;
}


return -1; // not found
}
}