package ref;

import org.w3c.dom.ls.LSOutput;

public class MethodChange1 {
    public static void main(String[] args){
        int a = 10;

        System.out.println("메서드 호출 전: a = " + a);
        changePrimitive(a);
        System.out.println("메서드 호출 후: a = " + a);
    }
    static void changePrimitive(int x){
        x = 20;
    }
}
