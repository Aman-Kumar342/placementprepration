public class linkedlidt{
    private Node head;
    private Node tail;
    public linkedlidt(){
        this.size=0;
    }

    private class Node{
        private int value;
        private Node next;
        public Node(int value){
            this.value=value;
        }
        public Node(int value,Node next){
            this.value=value;
            this.next=next;
        }
    }
    public static void main(String[] args) {
        
    }
}
