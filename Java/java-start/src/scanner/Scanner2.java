package scanner;

import java.util.Scanner;

public class Scanner2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("입력할 수 : ");
        int num1 = scanner.nextInt();

        System.out.print("입력할 수 : ");
        int num2 = scanner.nextInt();

        if (num1 > num2){
            System.out.print("더 큰수 : " + num1);
        } else if (num2 > num1) {
            System.out.print("더 큰수 : " + num2);
        }else {
            System.out.print("두 수는 같습니다.");
        }


    }
}
