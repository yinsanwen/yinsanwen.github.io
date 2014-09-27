Title: 动态规划在字符串上的应用
Date: 2014-07-21 18:43
Tags: 动态规划
Slug: using-dynamic-programing-in-string

#动态规划在字符串上的应用

> 动态规划可以解决一系列的字符串问题，下面总结了一些动态规划在字符串上的常见应用。

----
最长公共子串（sub-string）
------------------
求两个字符串的最长公共子串（连续的子串）。我们首先想到的应该是循环一个字符串，查找其中以每个字符开头的最长子串。在这之中，会有很多重复的计算过程。我们考虑使用动态规划来解决这个问题。

基本思路是：
两个字符串X，Y。长度分别为m，n。利用一个中间表L[m+1][n+1]。L[i][j]表示以Xi(Xi表示字符串X的第i个元素，非下标，下同)和Yj结尾的最长公共子串。那么我们就可以得到**状态转移方程**。

$$
L[i][j] = \begin{cases}
L[i-1][j-1] + 1 & X_i = Y_j \\
0 & X_i <> Y_j \end{cases}
$$
如果Xi和Yi相等，则以Xi和Yj结尾的公共子串的长度为以$X_{i-1}$和$Y_{j-1}$结尾的公共子串的长度加1。如果不然，显然，结果为0。

有了状态转移方程，就好写动态规划算法了。
``` java
	public String LCSubStr(char[] X, char[] Y){
		int length = 0;			//记录最长子串的长度
		int endX = 0;			//记录在X字符串中的结束位置
		//中间矩阵L
		//L[i][j]表示已Xi和Yj为结尾的相同子串的最大长度。
		//i,j不表示下标，表示第i,j个元素。
		int[][] L = new int[X.length+1][Y.length+1];
		for(int i = 0; i < X.length+1; i++){
			L[i][0] = 0;
		}
		for(int i = 0; i< Y.length+1; i++){
			L[0][i] = 0;
		}
		for(int i = 1; i < X.length+1; i++){
			for(int j = 1; j < Y.length+ 1; j++){
				if(X[i-1] == Y[j-1]){
					L[i][j] = L[i-1][j-1] + 1;
					if(L[i][j] > length){
						endX = i-1;
						length = L[i][j];
					}
				}else{
					L[i][j] = 0;
				}
			}
		}
		if(length == 0)return "";
		
		StringBuffer sb = new StringBuffer();
		for(int i = (endX-length+1); i <= endX; i++)
			sb.append(X[i]);
		return sb.toString();
	}
```

上面的代码在空间复杂度上面仍有改进的空间。因为我们的最外层循环是一行一行的处理，处理每一行时，只需要上一行的信息。因此我们没有必要使用$O(n^2)$的空间。只需要存储当前处理行的上一行即可。将空间复杂度将为$O(n)$。
``` java
static String longestSubString(String str1, String str2){
    //只需要两行的内存空间
    int[] preLine = new int[str2.length() + 1];
    int[] curLine = new int[str2.length() + 1];
    //记录最长公共子串的长度和结束位置
    int longestLength = -1, str1EndPoint = -1;
    for(int i = 0; i < str2.length() + 1; i++)preLine[i] = 0;
    for(int i = 0; i < str1.length(); i++){
    	curLine[0] = 0;
    	for(int j = 0; j < str2.length(); j++){
    		if(str1.charAt(i) == str2.charAt(j)){
    			curLine[j + 1] = preLine[j] + 1;
    			if(curLine[j + 1] > longestLength){
    				longestLength = curLine[j+1];
    				str1EndPoint = i;
    			}
    		}else
    			curLine[j + 1] = 0;
    	}
    	//将当前行变为上一行，为下次循环做准备
    	int[] tmp = preLine;
    	preLine = curLine;
    	curLine = tmp;
    }
    return str1.substring(str1EndPoint - longestLength + 1, str1EndPoint + 1);
}
```


最长公共子序列LCS（Longest Common Subsequence）
------------------


最短编辑距离(Shortest Edit Path)
-----------------
计算字符串a和字符串b的编辑距离，假设a长度为i，表示为a[1...i]；b长度为j，表示为b[1...j]。
考虑可操作的三种情况：
1. 插入：在字符串a的后面插入一个字符，使得和b字符串相等。
这一前提条件是a[1...i]和b[1...j-1]相等。
2. 删除：删除字符串a最后面的一个字符，使得和b字符串相等。
这一前提条件是a[1...i-1]和b[1...j]相等。
3. 替换：替换字符串a最后面的一个字符，使得和b字符串相等。
这一前提条件是a[1...i-1]和b[1...j-1]相等。

这里面涉及到子问题的最优解，适用于动态规划算法。
假设F[i,j]表示字符串A的前i位，和字符串B的前j位的最短编辑距离，则根据上面的分析，在上面三种情况中选择计算结果最小的值就是F[i,j]的值。有
$$ F[i,j] = min \begin{cases}
F[i][j-1]+1 & 插入 \\
F[i-1][j]+1 & 删除 \\
F[i-1][j-1] + \begin{cases}0 & A[i]=B[j] \\ 1 & A[i] != B[j] \end{cases} & 替换
\end{cases}
$$

程序代码如下：
``` java

	public static int shortestEditPath(String A, String B){
		int aLen = A.length(), bLen = B.length();
		int[][] F = new int[aLen+1][bLen+1];
		
		//初始化:有F[0][j] = j; F[i][0] = i;
		for(int i = 0; i <= aLen; i++){
			F[i][0] = i;
		}
		for(int j = 0; j <= bLen; j++){
			F[0][j] = j;
		}
		
		for(int i = 1; i <= aLen; i++){
			for(int j = 1; j <= bLen; j++){
				//三种操作各自所需的最短距离
				int insertDis = F[i][j-1] + 1;
				int deleteDis = F[i-1][j] + 1;
				int subsitWeight = A.charAt(i-1) == B.charAt(j-1) ? 0 : 1;
				int subsitDis = F[i-1][j-1] + subsitWeight;
				//取最小值
				int min = insertDis < deleteDis ? insertDis : deleteDis;
				if(subsitDis < min ) min = subsitDis;
				F[i][j] = min;
			}
		}
		return F[aLen][bLen];
		
	}
```






> Written with [StackEdit](https://stackedit.io/).