Title: 使用Spring的Mail组件发送邮件
Date: 2014-04-08
Category: Java Web
Tags: Spring, Mail
Slug: send-email-using-spring

很多场合我们都需要在我们的系统中使用发送邮件的功能，虽然JAVA提供了`JavaMail`可供使用，但是Spring也在其框架中提供了更高层的邮件组件。在Spring中发送邮件主要使用**`org.springframework.mail.javamail.JavaMailSenderImpl`**这个类。使用JavaMailSenderImpl，需要`org.springframework.context.support-3.0.5.RELEASE.jar`这个jar包。

首先看一看这个类的API说明

>   *public class JavaMailSenderImpl *
    *extends Object*
    *implements JavaMailSender*
>    
>    Production implementation of the JavaMailSender interface, supporting both JavaMail       MimeMessages and Spring SimpleMailMessages. Can also be used as a plain MailSender        implementation

可以看到我们可以是使用JavaMailSenderImpl发送`MimeMessages`和`SimpleMailMessages`。
在JavaMailSenderImpl中就提供了发送这两种信息的方法。
> *void send(MimeMessage mimeMessage)*  
&nbsp;&nbsp;Send the given JavaMail MIME message.

> *void send(SimpleMailMessage simpleMessage)*  
&nbsp;&nbsp;Send the given simple mail message.

###基本步骤###

1. 拿到一个`JavaMailSenderImpl`实例。我们可以在自己的代码中new一个JavaMailSenderImpl对象，也可以将JavaMailSenderImpl声明成一个bean，放在Spring的容器中。

2. 构造一个MimeMessages或者SimpleMailMessages实例。包含邮件的相关信息。

3. 使用 JavaMailSenderImpl 的send()方法，发送MimeMessages或者SimpleMailMessages。

下面我们根据实例说明JavaMailSenderImpl的用法.

----------

### step 1 ###
在spring的配置文件中声明JavaMailSenderImpl，并配置其有关的属性。

``` xml 
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:context="http://www.springframework.org/schema/context"
	xsi:schemaLocation="
			http://cxf.apache.org/core http://cxf.apache.org/schemas/core.xsd
			http://www.springframework.org/schema/beans 
			http://www.springframework.org/schema/beans/spring-beans.xsd
			http://www.springframework.org/schema/context 
    		http://www.springframework.org/schema/context/spring-context-3.0.xsd">

	<!-- 设置默认的邮件属性 -->
	<bean id="mailSenderImpl" class="org.springframework.mail.javamail.JavaMailSenderImpl">
		<property name="host" value="smtp.qq.com" />
		<!-- <property name="port" value="465" /> -->
		<property name="username" value="267237033@qq.com" />
		<property name="password" value="########" />
		<property name="javaMailProperties">
			<props>
				<prop key="mail.debug">true</prop>
				<prop key="mail.smtp.auth">true</prop>
			</props>
		</property>
	</bean>
	
	<!-- 声明我们自己构造的bean -->
	<bean id="myMailSender" class="spring.mail.demo.MyMailSender"></bean>

</beans>
```

### step 2 ###
声明我们的service类，调用JavaMailSenderImpl的方法。
``` java 
package spring.mail.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.MailSender;
import org.springframework.mail.SimpleMailMessage;

public class MyMailSender {

	@Autowired
	MailSender mailSender;
	
	/* 重新封装了JavaMailSenderImpl的send方法 */
	public void sendMail(String to, String subject, String body) {
		SimpleMailMessage message = new SimpleMailMessage();
		message.setFrom("267237033@qq.com");
		message.setTo(to);
		message.setSubject(subject);
		message.setText(body);
		mailSender.send(message);
	}
}
```
### step 3 ###
使用JUint对该方法进行测试。
``` java
package spring.mail.demo;


import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration("classpath:applicationContext.xml")
public class MailSenderTest {
	
	@Autowired
	private MyMailSender myMailSender;
	
	@Test
	public void testMyMailSender(){
		myMailSender.sendMail("yinsanwen@gmail.com", "Test Subjuect", "Test body ");
		System.out.println("email send ok.");
	}

}
```
关于如何使用JUint测试Spring项目。可以参考[使用JUnit测试Spring项目][1]




  [1]: http://about:blank
  
  
