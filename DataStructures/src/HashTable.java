public class HashTable {

    private HashNode[] buckets;
    private int numOfBuckets;
    private int size;

    public HashTable(int capacity){
        this.numOfBuckets=capacity;
        this.buckets=new HashNode[numOfBuckets];
        this.size=0;

    }

    public class HashNode{
        private Integer Key;
        private String Value;
        private HashNode next;

        public HashNode(Integer Key, String Value){
            this.Key=Key;
            this.Value=Value;




        }
    }

    public int getBucketIndex(Integer Key,int numOfBuckets){
        return Key%numOfBuckets;
    }

    public void put(Integer Key, String Value){

        int bucketIndex=getBucketIndex(Key,numOfBuckets);
        HashNode head=buckets[bucketIndex];

        while(head!=null){
            if(head.Key.equals(Key)){
                head.Value=Value;
                return;
            }
            head=head.next;
        }
        size++;
       head=buckets[bucketIndex];
       HashNode node=new HashNode(Key, Value);
       node.next = head;
       buckets[bucketIndex]=node;




    }

    public boolean IsEmpty(){
        return size==0;
    }
    public int size(){
        return size;
    }

    public String get(Integer key){

        int bucketIndex=getBucketIndex(key,numOfBuckets);
         HashNode head=buckets[bucketIndex];
         while(head!=null){
             if(head.Key.equals(key)){
                 return head.Value;
             }

         }return null;


    }

    public String remove(Integer key){

        int bucketIndex=getBucketIndex(key,numOfBuckets);
        HashNode head=buckets[bucketIndex];
        HashNode previous=null;
        while(head!=null){

            if(head.Key.equals(key)){

                break;
            }
            previous=head;
            head=head.next;
        }
        size--;

        if(head==null){
            return null;
        }
        if(previous!=null){
            previous.next=head.next;
        } else{
            buckets[bucketIndex]=head.next;
        }
        return head.Value;
    }

    public static void main(String[] args) {
        HashTable table = new HashTable(10);
        table.put(105, "Tom");
        table.put(21, "Harry");


        System.out.println(table.size());

        System.out.println(table.get(21));


    }

}
