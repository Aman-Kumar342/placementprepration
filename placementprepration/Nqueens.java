import  java.util.*;
public class Nqueens{
    public static void solve(int n){
        placeQueens(new int [n] ,0);
    }
    static void placeQueens(int []board,int row){
        if(row==board.length){
            printBoard(board);
            return;
        }
        for(int col=0;col<board.length;col++){
            if(issafe(board,row,col)){
                board[row]=col;
                placeQueens(board, row+1);
            }
        }
    }
    static boolean issafe(int []board,int row,int col){
        for(int i=0;i<row;i++){
            if(board[i]==col || Math.abs(board[i]-col)==Math.abs(i-row)){
                return false;
            }
        }
        return true;
    }
    static void printBoard(int []board){
        for(int row:board){
            System.out.println(".".repeat(row)+"Q"+".".repeat(board.length-row-1));
        }
        System.out.println();
    }
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        solve(n);
    }
}

