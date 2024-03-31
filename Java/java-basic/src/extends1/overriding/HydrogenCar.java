package extends1.overriding;

public class HydrogenCar extends Car {
    public void fillHydrogen() {
        System.out.println("수소를 충전합니다.");
    }

    @Override
    public void move() {
        System.out.println("전기차를 빠르게 이동합니다.");
    }
}
