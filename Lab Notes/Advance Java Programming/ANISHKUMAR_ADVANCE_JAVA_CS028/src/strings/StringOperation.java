package strings;


class Student{
	int rollno;
	String name;
	String city;
	Student(int rollno, String name, String city){
		this.rollno=rollno;
		this.name=name;
		this.city=city;
	}
	public String toString(){
		return rollno+" "+name+" "+city;
	}



public class StringOperation {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// Creation of String		
		System.out.println("\nCreation of String\n");
		char chars[] = { 'a', 'b', 'c', 'd', 'e', 'f' };
		String s = new String(chars, 2, 3);
		System.out.println("Value of s is "+ s);
		
		// Creation of String with ASCII Value
		System.out.println("\nCreation of String with ASCII Value\n");
		byte ascii[] = {65, 66, 67, 68, 69, 70 };
		String s1 = new String(ascii);
		System.out.println(s1);
		
		// Concatenation by "+"		
		System.out.println("\nConcatenation by \"+\" method\n");
		String s2="ACIT" +"Engineering";
		System.out.println(s2);
		
		// Concatenation by concat()
		System.out.println("\nConcatenation by concat() method\n");
		String s3="Acharya ";
		String s4=" Institute";
		String s5=s3.concat(s4);
		System.out.println(s5);
		
		// For toString() method
		System.out.println("\nFor toString() method\n");
		Student s6 =new Student(101,"Raj","lucknow");
		System.out.println(s6);
		
		// For CharAt()
		System.out.println("\nFor CharAt() method\n");
		String name="Acharya";
		char ch=name.charAt(4);
		System.out.println(ch);
		
		// For getChars()
		System.out.println("\nFor getChars() method\n");
		String str = new String("Hello Kumar how r u");
		char[] ch1 = new char[10];
		str.getChars(6, 16, ch1, 0);
		System.out.println(ch);
		
		//	For getBytes()	
		System.out.println("\nFor getBytes() method\n");
		String s7="ABCDEFG";
		byte[] barr=s7.getBytes();
		for(int i=0;i<barr.length;i++){
			System.out.println(barr[i]);
		}
		
		// For toCharArray()	
		System.out.println("\nFor toCharArray() method\n");
		String s8="hello";
		char[] ch2=s8.toCharArray();
		for(int i=0;i<ch2.length;i++) {
			System.out.println(ch2[i]); 
		}
		
		// For equals() and equalsIgnoreCase()
		System.out.println("\nFor equals() and equalsIgnoreCase() method\n");
		String s9="Kumar";
		String s10="KUMAR";
		System.out.println(s9.equals(s10));
		System.out.println(s9.equalsIgnoreCase(s10)); 
		
		//	For "==" method	
		System.out.println("\nFor \"==\" method	\n");
		String s11="Kumar";
		String s12=new String("Kumaa");
		System.out.println(s11==s12);
		
		// For compareTo() method
		System.out.println("\nFor compareTo() method\n");
		String s13="Sachin";
		String s14="Ratan";
		System.out.println(s13.compareTo(s14));
		
		// For startsWith() method
		System.out.println("\nFor startsWith() method\n");
		String s15="java string split method";
		System.out.println(s15.startsWith("java string"));
		
		// For endsWith() method
		System.out.println("\nFor endsWith() method\n");
		String s16="Acharya Institute of technology";
		System.out.println(s16.endsWith("yt"));
		
		// For indexOf() method
		System.out.println("\nFor indexOf() method\n");
		String s17="this is index of example";
		int index1=s17.indexOf("is");
		int index2=s17.indexOf("index");
		System.out.println(index1+" "+index2);
		
		// For lastIndexOf() method
		System.out.println("\nFor lastIndexOf() method\n");
		String s18="this is index of example";
		index1=s18.lastIndexOf('s');
		System.out.println(index1);
		
		// For substring() method	
		System.out.println("\nFor substring() method\n");
		String s19="SachinTendulkar";
		System.out.println(s19.substring(6));
		System.out.println(s19.substring(0,6));

		// For replaceString() method
		System.out.println("\nFor replaceString() method\n");
		String s20="AST is a very good college";
		String replaceString=s20.replace('S','I');
		System.out.println(replaceString);

		// For replace() method
		System.out.println("\nFor replace() method\n");
		String s21="my name is ABC my name is college";
		String replace1 =s21.replace("is","was");
		System.out.println(replace1);
		
		// For trim() method		
		System.out.println("\nFor trim() method\n");
		String s22=" hello string ";
		System.out.println(s22+"java");
		System.out.println(s22.trim()+"java");

		// For toLowerCase() and toUpperCase() method
		System.out.println("\nFor toLowerCase() and toUpperCase() method\n");
		String string1="Acharya Institute of Technology";
		String s1lower=string1.toLowerCase();
		System.out.println(s1lower);
		String s1upper=string1.toUpperCase();
		System.out.println(s1upper);
		
		// For StringBuffer() with append() method
		System.out.println("\nFor StringBuffer() with append() method\n");
		StringBuffer sb=new StringBuffer("Hello ");
		sb.append("AIT");
		System.out.println(sb);

		// For StringBuffer() with insert() method
		System.out.println("\nFor StringBuffer() with insert() method\n");
		StringBuffer sb1=new StringBuffer("Hello ");
		sb1.insert(1,"AIT");
		System.out.println(sb1);
		
		// For StringBuffer() with replace() method
		System.out.println("\nFor StringBuffer() with replace() method\n");
		StringBuffer sb2=new StringBuffer(" Hello World ");
		sb2.replace( 6, 11, "java");
		System.out.println(sb2); 

		// For StringBuffer() with delete() and deleteCharAt() method
		System.out.println("\nFor StringBuffer() with delete() and deleteCharAt() method\n");
		StringBuffer sb4=new StringBuffer("Hello");
		sb4.delete(1,3);
		System.out.println(sb4);
		
		StringBuffer sb5=new StringBuffer("This is a Test");
		sb5.deleteCharAt(3);
		System.out.println(sb5);
		
		// For StringBuffer() with replace() method
		System.out.println("\nFor StringBuffer() with replace() method\n");
		StringBuffer str1 = new StringBuffer("Hello");
		str1.reverse();
		System.out.println(str1);

		// For StringBuffer() with capacity() and ensureCapacity() method
		System.out.println("\nFor StringBuffer() with capacity() and ensureCapacity() method\n");
		StringBuffer str2 = new StringBuffer();
		System.out.println( str2.capacity());
		
		str2.ensureCapacity(30);
		System.out.println( str2.capacity());
		
		// For StringBuffer() with capacity() and length() method
		System.out.println("\nFor StringBuffer() with capacity() and length() method\n");
		StringBuffer s23=new StringBuffer("AIT");
		int p=s23.length();
		int q=s23.capacity();
		System.out.println("Length of string AIT="+p);
		System.out.println("Capacity of string AIT="+q);

		//	For StringBuffer() with  charAt() and setCharAt() method
		System.out.println("\nFor StringBuffer() with  charAt() and setCharAt() method\n");
		StringBuffer sb6 = new StringBuffer("Hello");
		System.out.println("buffer before = " + sb6);
		System.out.println("charAt(1) before = " + sb6.charAt(1));
		sb6.setCharAt(1, 'i');
		sb6.setLength(2);
		System.out.println("buffer after = " + sb6);
		System.out.println("charAt(1) after = " + sb6.charAt(1));
	}

}
}
