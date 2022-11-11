public class SinglyLinkedList {

    private ListNode head;

    private static class ListNode {
        private int data;
        private ListNode next;


        public ListNode(int data) {
            this.data = data;
            this.next = null;
        }

    }

    // ****print element of a Singly Linked List****

    public void display(){

        ListNode current = head;
        while(current!= null){
            System.out.print(current.data + "--->");
            current = current.next;
        }
        System.out.println("null");
    }

    // ****Length of a Singly Linked List in Java ****

    public int length(){
        if(head ==null){
            return 0;
        }
        int count = 0;
        ListNode current = head;

        while(current!=null){
            count++;
            current = current.next;
        }
        return count;
    }

    //****Insert node at the beginning****

    public void insertFirst( int value){
        ListNode newNode = new ListNode(value);
        newNode.next = head;
        head = newNode;

    }

    //****Insert node at the End ****

    public void insertLast(int value){
        ListNode newNode = new ListNode(8);
        if(head == null){
            head = newNode;
            return;
        }
        ListNode current = head;
        while (null!=current.next){
            current = current.next;
        }
        current.next = newNode;


    }



    public static void main(String[] args) {
        SinglyLinkedList sll = new SinglyLinkedList();
        sll.head = new ListNode(10);
        ListNode second = new ListNode(1);
        ListNode third = new ListNode(8);
        ListNode fourth = new ListNode(11);

        //Now we will connect them together to form a chain

        sll.head.next = second;
        second.next = third;
        third.next = fourth;

        sll.insertFirst(11);
        sll.insertFirst(8);
        sll.insertFirst(1);

        sll.display();
        System.out.println("Length is - " +sll.length());


    }

}
