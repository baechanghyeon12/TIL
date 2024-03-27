package oop1;

public class ValueDataMain {
    public static void main(String[] args) {

        ValueData valueData = new ValueData();
        for (int i = 0 ; i < 10;i++){
        valueData.add();
        }
        System.out.println("최종 숫자=" + valueData.value);
    }
}

