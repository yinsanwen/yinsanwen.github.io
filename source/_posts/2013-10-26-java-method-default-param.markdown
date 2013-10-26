---
layout: post
title: "Java中默认参数的实现——使用方法的重载"
date: 2013-10-26 17:00
comments: true
categories: 
---
### Java不支持为方法设置默认的参数

例如，我想定义一个获取用户最近一段时间内用户行为的方法，定义如下：
``` java 	
	/**
	 * 获取所有用户最近一段时间内对itemID的浏览记录
	 * @param itemID 
	 * @param limit 限定值
	 * @param unit	限定单位为"MONTH","DAY",默认为MONTH
	 * @return
	 */
	long[] browseHistory(long itemID, int limit, String unit = 'MONTH');
```
Eclipse会报错，不支持为unit设置默认值“MONTH”。
可以使用方法的重载机制。如下：
``` java
	/**
	 * 方法的重载，定义一个只有两个参数的browseHistory方法，再设置默认值调用目标方法。
	 * @param itemID
	 * @return
	 */
	long[] browseHistory(long itemID, int limit){
		return browseHistorty(itemID, limit, 'MONTH');
	}
	
	/**
	 * 获取所有用户最近一段时间内对itemID的浏览记录
	 * @param itemID 
	 * @param limit 限定值
	 * @param unit	限定单位为"MONTH","DAY",默认为MONTH
	 * @return
	 */
	long[] browseHistory(long itemID, int limit, String unit);
```
