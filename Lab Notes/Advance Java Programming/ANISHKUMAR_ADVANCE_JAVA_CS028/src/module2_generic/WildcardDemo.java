package module2_generic;
class Stats<T extends Number>{
	T[] nums;
	Stats(T[] o){
		nums = o;
	}
	double average() {
		double sum =0.0;
		for(int i=0;i<nums.length;i++) {
			sum+= nums[i].doubleValue();
		}
		return sum/nums.length;
	}
	boolean sameAvg(Stats<?> ob) {
		if(average()== ob.average())
			return true;
		return false;
	}
}
public class WildcardDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Integer inums[] = {1,2,3,4,5};
		Stats<Integer>iob=new Stats<Integer>(inums);
		double v = iob.average();
		System.out.println("iob average is "+v);
		
		Double dnums[] = {1.1,2.2,3.3,4.4,5.5};
		Stats<Double>dob=new Stats<Double>(dnums);
		double v1 = dob.average();
		System.out.println("dob average is "+v1);
		
		Float fnums[] = {1.1F,2.2F,3.3F,4.4F,5.5F};
		Stats<Float>fob=new Stats<Float>(fnums);
		double v2 = fob.average();
		System.out.println("fob average is "+v2);
		
		System.out.println("Same Average is");
		if(iob.sameAvg(dob))
			System.out.println("Yes");
		else
			System.out.println("No");
	}

}