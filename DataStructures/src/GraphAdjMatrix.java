public class GraphAdjMatrix {
    int V;
    int E;
    int[][] adjMatrix;

    public GraphAdjMatrix(int nodes){
        this.V=nodes;
        this.E=0;
        this.adjMatrix = new int[nodes][nodes];
    }
    public void addEdge(int V, int E){

        adjMatrix[E][V]=1;
        adjMatrix[V][E]=1;
        E++;

    }
    public String toString(){
        StringBuilder sb= new StringBuilder();
        sb.append(V +"vertices"+ E+ "edges" +"\n");
        for(int v=0;v<V;v++){
            sb.append(v + ":");
            for(int w:adjMatrix[v]){

                sb.append(w+" ");

            }
            sb.append("\n");
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        GraphAdjMatrix Graph = new GraphAdjMatrix(4);
        Graph.addEdge(0,1);
        Graph.addEdge(1,2);
        Graph.addEdge(2,3);
        Graph.addEdge(3,0);
        System.out.println(Graph);
    }
}
