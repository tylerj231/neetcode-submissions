class DynamicArray {
    private int size = 0;
    private int [] array;

    public DynamicArray(int capacity) {
        this.array = new int [capacity];
    }

    public int get(int i) {
        return array[i];

    }

    public void set(int i, int n) {
        this.array[i] = n;
    }

    public void pushback(int n) {
        if (this.size >= this.array.length) {
            resize();
        }
        this.array[size] = n;
        size++;
    }

    public int popback() {
        int removedElement = this.array[size - 1];
        this.array[size - 1] = 0;
        this.size--;
        return removedElement;
    }

    private void resize() {
        int currentCapacity = this.array.length; 
        int [] oldArray = this.array;
        int [] newArray = new int [currentCapacity * 2];

        for (int i = 0; i < this.size; i++) {
            newArray[i] = oldArray[i];
        }
        this.array = newArray;

    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.array.length;
    }
}
