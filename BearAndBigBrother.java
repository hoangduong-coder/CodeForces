import java.util.*;
public class BearAndBigBrother {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String input = sc.nextLine();
		String[] values = input.split("\\ ");
		int Limak = Integer.parseInt(values[0]);
		int Bob = Integer.parseInt(values[1]);
		int year = 0;
		while (Limak <= Bob) {
			Limak *= 3;
			Bob *= 2;
			year += 1;
		};
		System.out.println(year);
	}
}
