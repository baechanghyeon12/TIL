package extends1.overriding;

public class CarMain {
    public static void main(String[] args) {
        ElectricCar electricCar = new ElectricCar();
        electricCar.move();
        electricCar.charge();
        electricCar.openDoor();

        GasCar gasCar = new GasCar();
        gasCar.move();
        gasCar.fillUp();
        gasCar.openDoor();

        HydrogenCar hydrogenCar = new HydrogenCar();
        hydrogenCar.move();
        hydrogenCar.fillHydrogen();
        hydrogenCar.openDoor();

        // 오버로딩
        //이름은 같지만 시그니처(파라미터 수, 타입) 데는 다른 메소드를 중복으로 선언하는 것을 의미


        // 오버라이
        // 부모 클래스의 메소드의 동작 방법을 변경(재정의)하여 우선적으로 사용하는 것
    }
}
