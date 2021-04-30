package codeforces;
import java.util.*;
public class HelpfulMaths {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String sum = sc.nextLine();
		String[] terms = sum.split("\\+");
		Arrays.sort(terms);
		for(int i=0;i<terms.length;i++) {
			System.out.print(terms[i]);
			if(i == terms.length - 1) break;
			System.out.print("+");
		}
	}
}
