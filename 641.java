class MyCircularDeque {
    private int head, tail, size, n;
    private final int[] a;
    public MyCircularDeque(int k) {
        a = new int[k];
        n = a.length;
        tail = 1;
    }
    
    public boolean insertFront(int x) {
        if (size == n) return false;
        a[head = ++head % n] = x;
        size++;
        return true;
    }
    
    public boolean insertLast(int x) {
        if (size == n) return false;
        a[tail = (--tail + n) % n] = x;
        size++;
        return true;
    }
    
    public boolean deleteFront() {
        if (size == 0) return false;
        head = (--head + n) % n;
        size--;
        return true;
    }
    
    public boolean deleteLast() {
        if (size == 0) return false;
        tail = ++tail % n;
        size--;
        return true;
    }
    
    public int getFront() {
        return size == 0 ? -1 : a[head];
    }
    
    public int getRear() {
        return size == 0 ? -1 : a[tail];
    }
    
    public boolean isEmpty() {
        return size == 0;
    }
    
    public boolean isFull() {
        return size == a.length;
    }
}
