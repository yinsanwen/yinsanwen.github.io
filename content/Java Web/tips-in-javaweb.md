Title: tips-in-javaweb 
Date: 2014-04-08
Tags: properties
Slug: tips-in-javaweb

[TOC]

## Tip 1. 使用配置文件 ##
定义一个配置文件，存放需要配置的信息。假设文件名为config.properties。
``` xml
# email configuration #
system.email=xxxxxx@qq.com
system.email.pwd=ysw******

```
如何使用该配置文件？

### 方法一 在Spring的配置文件xml中使用 ###

1. 使用`<context:property-placeholder />`标签，加载配置文件。

2. 在需要的地方通过`${name}`来使用。

实例：
``` xml
<!-- 加载配置文件 -->
<context:property-placeholder location="classpath:config.properties"/>

<!-- email start -->
	<bean id="mailSender" class="org.springframework.mail.javamail.JavaMailSenderImpl">
		<property name="host" value="smtp.qq.com" />
		<property name="defaultEncoding" value="UTF-8" />
		<property name="username" value="${system.email}" />
		<property name="password" value="${system.email.pwd}" />
		<property name="javaMailProperties">
			<props>
				<prop key="mail.debug">true</prop>
				<prop key="mail.smtp.auth">true</prop>
			</props>
		</property>
	</bean>
```

### 方法二 使用`java.util.Properties`类 ###
1. 使用单例模式创建Properties工厂类。

2. 使用工厂得到一个Properties实例，得到属性值。

实例：
``` java
package com.neuropeptide.tools;

import java.io.InputStream;
import java.util.Properties;

/**
 * 单例模式读取属性配置文件
 * @author HF
 *
 */
public class PropertiesFactoryHelper {

	private static PropertiesFactoryHelper _instance = null;
	private Properties properties = new Properties();

	/**
	 * 私有构造方法
	 */
	private PropertiesFactoryHelper() {

		try {
			InputStream inputStream = this.getClass().getResourceAsStream("/config.properties");
			properties.load(inputStream);
			if (inputStream != null)
				inputStream.close();
		} catch (Exception e) {
			System.out.println(e + "file not found");
		}
	}
	
	/**
	 * 单例静态工厂方法
	 * @return
	 */
	synchronized public static PropertiesFactoryHelper getInstance(){
		if(_instance == null)
			_instance = new PropertiesFactoryHelper();
		return _instance;
	}

	/**
	 * 读取配置信息
	 */
	public String getConfig(String key){
		return properties.getProperty(key);
	}
	
}
```
在需要的类中使用上面的工厂得到实例，并进行取值。
``` java
PropertiesFactoryHelper propeties = PropertiesFactoryHelper.getInstance();

String systemEmail = propeties.getConfig("system.email");
```
