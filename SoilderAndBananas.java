import java.util.*;
public class SoilderAndBananas {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String inputLine = sc.nextLine();
		String[] numbers = inputLine.split("\\ ");
		int firstBanana = Integer.parseInt(numbers[0]);
		int money = Integer.parseInt(numbers[1]);
		int numBananas = Integer.parseInt(numbers[2]);
		int total = 0;
		int result = 0;
		for(int i=1; i<=numBananas; i++) {
			total += i*firstBanana;
		}
		if(total > money) {
			result = total - money;
		}
		else {
			result = 0;
		}
		System.out.println(result);
	}
}
