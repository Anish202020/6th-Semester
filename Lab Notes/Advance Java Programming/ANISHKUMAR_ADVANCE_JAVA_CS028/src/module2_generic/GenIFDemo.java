package module2_generic;
interface MinMax<T extends Comparable<T>>{
	T min();
	T max();
}
class MyClass<T extends Comparable<T>> implements MinMax<T>{
	T[] vals;
	MyClass(T[]  o){vals=o;}
	
	public T min() {
		T v = vals[0];
		for(int i=1;i<vals.length;i++)
				if(vals[i].compareTo(v)<0)
					v=vals[i];
		return v;
	}
	
	public T max() {
		T v = vals[0];
		for(int i=1;i<vals.length;i++)
				if(vals[i].compareTo(v)>0)
					v=vals[i];
		return v;
	}
}
public class GenIFDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Integer inums[]= {3,6,2,8,6};
		Character chs[]= {'b','r','P','W'};
		MyClass<Integer>iob=new MyClass<Integer>(inums);
		MyClass<Character>cob=new MyClass<Character>(chs);
		System.out.println("Max Value of inums "+iob.max());
		System.out.println("Min Value of inums "+iob.min());
		System.out.println("Max Value of chs "+cob.max());
		System.out.println("Min Value of chs "+cob.min());
		
		
	}

}
