package DSAImplementations;


public class SinglyLinkedList{
    ListNode head;

    private static class ListNode{
        private int data;
        private ListNode next;
         private ListNode(int data){
             this.data=data;
             this.next=null;
         }


    }

    private void display(){
        if(head==null){
            return;
        }
        ListNode current=head;
        while(current!=null){
            System.out.print(current.data+ "--->");
            current=current.next;
        }
        System.out.println("null");
    }
    private int length(){
        if (head.next==null){
            return-1;
        }
            int count=0;
        ListNode current=head;
        while(current!=null){
            count+=1;
            current=current.next;
        }
return count;
    }
    private void insertInBeginning(){
        ListNode newnode= new ListNode(199);
        newnode.next=head;
        head=newnode;
    }

    public void insertInEnd (){
        ListNode newnodeforend = new ListNode(675);
        if (head==null){
            head=newnodeforend;
        }
        ListNode current = head;
        while(current.next!=null){

            current=current.next;
        }
        current.next=newnodeforend;

    }
    public static void main(String[] args) {
        SinglyLinkedList ss=new SinglyLinkedList();
        //ss.head=new ListNode(10);
        ListNode first= new ListNode(2);
        ss.head=first;
        ListNode second= new ListNode(20);
        ListNode third=new ListNode(50);
        ListNode fourth = new ListNode(77);
        ss.head.next=second;
        second.next=third;
        third.next=fourth;


        ss.insertInEnd();
        ss.insertInBeginning();
        ss.display();
        ss.length();

        System.out.println("Length of Linked List "+ ss.length());

    }
}