package demo.secure.coding;

public class MyCalculator {
	
	public int sum(int a, int b)
	{
		int c,d;
		c=20+30;
		return c;
	}
	public int diff(int a, int b)
	{
		return (a-b);
	}

	public static void main(String[] args) {
		MyCalculator ob = new MyCalculator();
		System.out.println("Sum is "+ob.sum(10, 5));
		System.out.println("Diff is "+ob.diff(10, 5));
	}
}
