package module2_generic;
class GenCons{
	private double val;
	<T extends Number>GenCons(T arg){
		val = arg.doubleValue();
	}
	void show() {
		System.out.println("Val is "+val);
	}
}
public class GenConsDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		GenCons test1 = new GenCons(100);
		GenCons test2 = new GenCons(100.11);
		test1.show();
		test2.show();
	}

}
