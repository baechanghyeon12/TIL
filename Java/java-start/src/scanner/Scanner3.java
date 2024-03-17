package scanner;

import java.util.Scanner;

public class Scanner3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("출력하고자 하는 단을 입력해주세요: ");
        int dan = input.nextInt();
        System.out.println("출력하고자 하는 단은 "+dan+"단입니다.");
        for (int i = 1; i < 10; i++){
            System.out.println(dan + "*" + i + "=" + dan * i);
        }
    }
}
