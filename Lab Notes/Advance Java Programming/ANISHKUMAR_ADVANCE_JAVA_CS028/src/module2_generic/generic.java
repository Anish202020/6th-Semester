package module2_generic;
class Gen<T>{
	T ob;
	Gen(T o) {	
	ob= o;
	}
	T getob() {
		return ob;
	}
	void showType() {
		System.out.println("Type T is "+ob.getClass().getName());
	}
}
public class generic {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Gen<Integer> iob = new Gen<Integer>(88);
		Gen<Double> iob1 = new Gen<Double>(88.0);
		iob.showType();
		int v = iob.getob();
		System.out.println("Value : "+v);
		iob1.showType();
		int v1 = iob.getob();
		System.out.println("Value : "+v1);
	}

}
