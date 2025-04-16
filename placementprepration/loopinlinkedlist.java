import java.util.Scanner;
class LinkedList {
    static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }
    Node head;
    // Function to add a node to the linked list
    public void addNode(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
        }
    }
    // Function to create a loop for testing
    public void createLoop(int position) {
        if (position == -1) return;
        Node temp = head, loopNode = null;
        int count = 1;
        while (temp.next != null) {
            if (count == position) {
                loopNode = temp;
            }
            temp = temp.next;
            count++;
        }
        temp.next = loopNode; // Create the loop
    }
    // Function to detect a loop using Floyd's Cycle Detection
    public boolean detectLoop() {
        Node slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;           // Move slow by one step
            fast = fast.next.next;      // Move fast by two steps

            if (slow == fast) {
                return true;            // Loop detected
            }
        }
        return false;                   // No loop
    }
    // Function to display the linked list (only useful for loop-free lists)
    public void display() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " -> ");
            temp = temp.next;
        }
        System.out.println("null");
    }
}
public class loopinlinkedlist {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        LinkedList linkedList = new LinkedList();
        System.out.println("Enter the number of nodes in the linked list:");
        int n = scanner.nextInt();
        System.out.println("Enter the node values:");
        for (int i = 0; i < n; i++) {
            linkedList.addNode(scanner.nextInt());
        }
        System.out.println("Enter the position to create a loop (-1 for no loop):");
        int position = scanner.nextInt();
        linkedList.createLoop(position);
        if (linkedList.detectLoop()) {
            System.out.println("Loop detected in the linked list.");
        } else {
            System.out.println("No loop detected in the linked list.");
        }

        scanner.close();
    }
}
