---
layout: post
title: "pl/sql conllections"
date: 2013-11-10 10:20
comments: true
categories: database
---

#PL/SQL 中的集合类型

PL/SQL 中有三种集合类型：`Varrays`, `Nested tables`, `Associative arrays`.  

- Varrays: 拥有固定的长度（虽说在运行时中可以改变），使用连续的数字作为下标。_类似Java语言中的数组，定长。_
- Nested tables: 可以拥有任意数量的元素，使用连续的数字作为下标。_类似Java语言中的List类型。_
- Associative arrays，又叫做`Index-by tables`。可以使用任意的数字或者字符串作为下标。_类似Java语言中的Map数据结构_  
<!-- more -->
Associative arrays**默认按索引的字母顺序排序**(alphabetically)。  

{% codeblock lang:sql  title:字符串索引默认用字母顺序排序 %}
DECLARE  TYPE population_type IS TABLE OF NUMBER INDEX BY VARCHAR2(64);
  country_population population_type;
  continent_population population_type;
  howmany NUMBER;
  which VARCHAR2(64);
BEGIN
  country_population('Greenland') := 100000; -- Creates new entry
  country_population('Iceland') := 750000;   -- Creates new entry
-- Looks up value associated with a string
  howmany := country_population('Greenland');
  continent_population('Australia') := 30000000;
  continent_population('Antarctica') := 1000; -- Creates new entry
  continent_population('Antarctica') := 1001; -- Replaces previous value 
-- Returns 'Antarctica' as that comes first alphabetically.
  which := continent_population.FIRST;
-- Returns 'Australia' as that comes last alphabetically.  which := continent_population.LAST;
-- Returns the value corresponding to the last key, in this
-- case the population of Australia.
  howmany := continent_population(continent_population.LAST);
END;
{% endcodeblock %}

{% codeblock lang:sql title:数字索引默认数字大小排序 %}
DECLARE 
  TYPE number_index_table IS TABLE OF NUMBER INDEX BY PLS_INTEGER;
  num_tab number_index_table ;
  which integer;
BEGIN
  num_tab(111) := 111;
  num_tab(222) := 111;
  num_tab(11) := 111;
  num_tab(22) := 111;
  num_tab(333) := 111;
  --loop num_tab
  which := num_tab.FIRST;
  while which is not null
  loop 
     DBMS_OUTPUT.PUT_LINE(which||'->'||num_tab(which));
     which := num_tab.NEXT(which);
  end loop;
END;
{% endcodeblock %}
输出
{% codeblock lang:bash %}
11->111
22->111
111->111
222->111
333->111
{% endcodeblock %}

##Collection的方法
前面使用了`First`,`Last`,`Next`等集合的方法。集合的方法一共包括 
>COUNT, DELETE, EXISTS, EXTEND, FIRST, LAST, LIMIT, NEXT, PRIOR, and TRIM.  

###需要注意的是:

- 集合的方法不能用在SQL语句中
- EXTEND 和 TRIM 不能用于Associative arrays
- EXISTS, COUNT, LIMIT, FIRST, LAST, PRIOR, 和 NEXT是函数；而EXTEND, TRIM, DELETE 是存储过程
- EXISTS, PRIOR, NEXT, TRIM, EXTEND, DELETE 带有表示下标的参数。 一般情况下下标都是数字，在Associative arrays中可以使字符串  

###下面对这些方法或是过程做些说明

-  **EXISTS(n)** : returns TRUE if the nth element in a collection exists.
-  **COUNT** : returns the number of elements that a collection currently contains.
-  **LIMIT** : 返回集合的最大容量。对于nested table 和associative arrays，没有固定的容量大小，返回NULL。对于Varrays，返回其容量大小。
-  **FIRST** : 返回集合的第一个（最小的）索引（下标），  
   **LAST** : 返回最后一个（最大的)索引（下标）。
-  **PRIOR(n)** : 返回索引n的前一个索引，  如果n是第一个索引，返回null；  
   **NEXT(n)** : 返回索引n的下一个索引，如果n是最后一个索引，返回null。
-  **EXTEND** : 增加集合的长度，对varray和nested array使用。有三种形式  
   - EXTEND 在集合末尾增加一个Null元素
   - EXTEND(n) 在集合末尾增加n个Null元素
   - EXTEND(n,i) 将集合的第i个元素的值复制n份到集合的末尾。  
     不能对index-by tables 使用extend。不能对未初始化的集合使用extend。
-  **TRIM** : 减少集合的容量，有两种形式
   - TRIM 除去集合末尾的最后一个元素
   - TRIM(n) 除去集合末尾的n个元素。  
     如果想删除所有的元素，使用不带参数的DELETE
- **DELETE** : 删除集合中的元素，有三种形式
   - DELETE 不带参数，删除集合中所有元素
   - DELETE(n) 删除下标为n的元素
   - DELETE(m,n) 删除所有下标在m...n之间的元素

