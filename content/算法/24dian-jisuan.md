Title: 24点算法的JAVA实现
Date: 2014-06-13 18:12
Tags: 递归 穷举
Slug: 24dian-jisuan


> 给定N个数,问能否通过`+ - * /`和括号`()`,使得计算结果等于24.

#### 算法思路
最常见的是使用穷举法,步骤如下:
① 从数组A[1..N]的N个数中选取两个数, 有C(N,2)中可能.
② 被选择的这两个数进行各种可能的运算:加法和乘法没有顺序,加法和除法有顺序.最多可以有6钟计算结果.
③ 将参与运算的两个数移除,并将计算结果放入数组A中.然后递归调用①.

**注意:** 在步骤①进行循环时,因为每次选择的两个数不一定正确,所以应该在第二步之前保存选择的数.并在下次循环之前恢复数组A.

---
源码如下:
``` java
import java.util.Scanner;

public class TwentyFour {
	/**
	 * 数组A的前n个数能否24点计算成功
	 * @param A
	 * @param n
	 */
	public static boolean twentyFour(double A[], int n, String[] exp){
		if(n == 1){
			if(A[0] == 24.0){
				return true;
			}else {
				return false;
			}
		}
		double a,b;
		String expa,expb;
	
		for(int i = 0; i < n; i++){
			for(int j = i+1; j < n; j++){
				//计算A[i]和A[j]的所有可能
				
				a = A[i];
				b = A[j];
				expa = exp[i];
				expb = exp[j];
				
				A[j] = A[n-1];
				exp[j] = exp[n-1];
				
				//①相加再判断
				A[i] = a + b;
				exp[i] = "(" + expa + " + " + expb + ")";
				if(twentyFour(A, n-1, exp)){
					return true;
				}
				//②想乘判断
				A[i] = a * b;
				exp[i] = "(" + expa + " * " + expb + ")";
				if(twentyFour(A, n-1,exp)){
					return true;
				}
				//③a-b
				A[i] = a - b;
				exp[i] = "(" + expa + " - " + expb + ")";
				if(twentyFour(A, n-1, exp)){
					return true;
				}
				//④b-a
				A[i] = b - a;
				exp[i] = "(" + expb + " * " + expa + ")";
				if(twentyFour(A, n-1,exp)){
					return true;
				}
				//⑤a / b
				if(b != 0.0){
					A[i] = a / b;
					exp[i] = "(" + expa + " / " + expb + ")";
					if(twentyFour(A, n-1, exp)){
						return true;
					}
				}
				//⑥ b / a
				if(a != 0.0){
					A[i] = b / a;
					exp[i] = "(" + expb + " / " + expa + ")";
					if(twentyFour(A, n-1, exp)){
						return true;
					}
				}
				
				//A[i]和A[j]的组合没有结果,继续下一次循环,继续之前,需要恢复现场给下次循环
				A[i] = a;
				A[j] = b;
				exp[i] = expa;
				exp[j] = expb;
			}
		}
		//所有循环结束没有找到计算方法,返回false
		return false;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		double[] A = new double[n];
		String[] exp = new String[n];
		for(int i = 0; i < n; i++){
			int x = sc.nextInt();
			A[i] = x;
			exp[i] = String.valueOf(x);
		}
		if(twentyFour(A, n, exp)){
			System.out.println(exp[0]);
		}else {
			System.out.println("NONE");
		}
	}
}
```



> Written with [StackEdit](https://stackedit.io/).