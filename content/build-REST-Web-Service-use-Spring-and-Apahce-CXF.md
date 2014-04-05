Title: 利用Spring和Apache CXF构建REST Web Service
Date: 2014-03-20 20:53
Category: j2EE
Tags: jax-rs,rest,cxf
Slug: build-REST-Web-Service-use-Spring-and-Apahce-CXF 
Author: sanween
Summary:

首先说一说JAX-RS，直接引用wiki上面的说明。
> **JAX-RS: Java API for RESTful Web Services**是一个Java编程语言的应用程序接口,支持按照**表象化状态转变**(REST)架构风格创建Web服务. JAX-RS使用了Java SE 5引入的Java 标注来简化Web服务客户端和服务端的开发和部署。

在J2EE 6中，已经引入对了JAX-RS的支持。在我的理解中，JAX-RS和JSR-311表示的是同一个标准规范。

而JAX-RS标准规范有多种不同的实现。主要包括  
Apache CXF, 开源的Web服务框架。  
Jersey, 由Sun提供的JAX-RS的参考实现  
RESTEasy，JBoss的实现  
Restlet，由Jerome Louvel和Dave Pawson开发，是最早的REST框架，先于JAX-RS出现。

好的，前面介绍了一些构建REST服务的背景，我们下面使用Apache CXF来完成REST服务的构建。  
因为Aapche CXF是高依赖于Spring的，我们也用到了Spring。  
（其实Spring也有自己的REST支持，不过具体是通过什么支持，还没有了解，以后有机会比较一下和本文采用方式的区别）。

## Step 1. 基本源代码

在这个Demo中，我们假设系统中有一些用户的信息，我们定义一个User实体类。然后开放REST接口，通过REST服务的方式对系统中的User进行CRUD
(Create, Read, Update, Delete)操作。

### Model层
定义User实体类，是一个简单的POJO

*User.java*  

``` java
package info.sanween.demo.rest.model;

import java.util.Date;

public class User {
	
	private Integer id;
	private String name;
	private String email;
	private Date birthDate;
	private String city;
	private String state;
	
	/*省略setters和getters方法*/
}
```

### Service层
为了例子的简单，我们没有定义Dao层，直接将User信息存放在内存中。

**定义JAX-RS Service类，在类名上使用@Path注解**。（该类是可以通过CXF暴露给外界的Service类）。  
*有关该类中的注解说明 以及POST,PUT,GET,DELETE对应的CRUD操作，请了解JAX-RS规范。*

*UserManager.java*  

``` java
package info.sanween.demo.rest.service;

import info.sanween.demo.rest.model.User;

import java.util.List;

import javax.ws.rs.Consumes;
import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;

@Path("/users")
public interface UserManager {
	
	//创建用户使用POST,需要创建的用户信息在HTTP的请求中说明
	@POST
	@Consumes("application/json")
	@Produces("application/json")
	public void createUser(User user);
	
	//读取用户使用GET,请求中带id
	@GET
	@Path("{id}")
	@Consumes("application/json")
	@Produces("application/json")
	public User readUser(@PathParam("id") Integer id);
	
	//更新用户使用PUT,请求中带id,需要更新的用户信息在HTTP的请求中说明
	@PUT
	@Path("{id}")
	@Consumes("application/json")
	@Produces("application/json")
	public void updateUser(@PathParam("id") Integer id, User user);
	
	//删除用户使用DELETE,请求中带id
	@DELETE
	@Path("{id}")
	@Consumes("application/json")
	@Produces("application/json")
	public void deleteUser(@PathParam("id") Integer id);
}
```

实现上面的Service  

*UserManagerService.java*  

``` java 
package info.sanween.demo.rest.service.impl;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicInteger;

import javax.ws.rs.WebApplicationException;
import javax.ws.rs.core.Response;

import info.sanween.demo.rest.model.User;
import info.sanween.demo.rest.service.UserManager;

public class UserManagerService implements UserManager {

	private Map<Integer, User> userDB = new ConcurrentHashMap<Integer, User>();
	private AtomicInteger idCounter = new AtomicInteger();

	@Override
	public void createUser(User user) {
		// TODO Auto-generated method stub
		Integer id = idCounter.incrementAndGet();
		user.setId(id);
		userDB.put(id, user);
		System.out.println("Created user " + id);
	}

	@Override
	public User readUser(Integer id) {
		// TODO Auto-generated method stub
		final User user = userDB.get(id);
		if(user == null){
			throw new WebApplicationException(Response.Status.NOT_FOUND);
		}
		return user;
	}

	@Override
	public void updateUser(Integer id, User user) {
		// TODO Auto-generated method stub
		User current = userDB.get(id);
		if(current == null)
			throw new WebApplicationException(Response.Status.NOT_FOUND);
		current.setBirthDate(user.getBirthDate());
		current.setName(user.getName());
		current.setCity(user.getCity());
		current.setEmail(user.getEmail());
		current.setState(user.getState());
	}

	@Override
	public void deleteUser(Integer id) {
		// TODO Auto-generated method stub
		User user = userDB.get(id);
		if(user == null)
			throw new WebApplicationException(Response.Status.NOT_FOUND);
		userDB.remove(id);
	}
}
```
上面的代码中，我们将User数据信息直接放置在内存之中。

## Step 2. 配置文件

好了，到目前为止。我们所需要编写的代码都已经完成了。接下来就是使用Spring和CXF调用这些代码。

在WEB-INF目录下创建rest-context.xml文件。在该配置文件中，定义REST的配置内容

*rest-content.xml*  
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:cxf="http://cxf.apache.org/core"
	xmlns:jaxws="http://cxf.apache.org/jaxws" xmlns:jaxrs="http://cxf.apache.org/jaxrs"
	xsi:schemaLocation="
			http://cxf.apache.org/core http://cxf.apache.org/schemas/core.xsd
			http://www.springframework.org/schema/beans 
			http://www.springframework.org/schema/beans/spring-beans.xsd
			http://cxf.apache.org/jaxrs http://cxf.apache.org/schemas/jaxrs.xsd
			http://cxf.apache.org/jaxws http://cxf.apache.org/schemas/jaxws.xsd">

	<!-- 添加cxf的配置文件 -->
	<import resource="classpath:META-INF/cxf/cxf.xml" />
	<import resource="classpath:META-INF/cxf/cxf-servlet.xml" />
	
	<!-- 创建一个jsonProvider给jaxrs:server元素使用 -->
	<bean id="jsonProvider" class="org.codehaus.jackson.jaxrs.JacksonJsonProvider" />

	<!-- 暴露我们将要提供的Rest服务 -->
	<jaxrs:server id="userManagerREST" address="/rest/UserManager">
		<jaxrs:serviceBeans>
			<ref bean="userManagerService" />
		</jaxrs:serviceBeans>
		<jaxrs:providers>
			<ref bean='jsonProvider' />
		</jaxrs:providers>
	</jaxrs:server>
	
	<!-- 这里定义我们所编写的Bean，你也可以使用注解的方式管理bean -->
	<bean id="userManagerService" class="info.sanween.demo.rest.service.impl.UserManagerService" />
</beans>
```
注意：使用`<jaxrs:server>`元素来暴露我们想要对外提供的接口。并注意其"address"属性，这是访问我们这个接口的路径。

接下来，我们在web.xml中声明使用Spring和定义CXF Servlet。

*web.xml*
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app version="3.0" xmlns="http://java.sun.com/xml/ns/javaee"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://java.sun.com/xml/ns/javaee 
	http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd"
	metadata-complete="true">

	<display-name>RestDemo</display-name>
	<description>RestDemo</description>

	<!-- begin Spring -->
	<context-param>
		<param-name>contextConfigLocation</param-name>
		<param-value>/WEB-INF/*-context.xml</param-value>
	</context-param>

	<listener>
		<listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
	</listener>
	<!-- end Spring -->
	
	<!-- 使用CXF servlet -->
	<servlet>
		<servlet-name>CXFServlet</servlet-name>
		<servlet-class>org.apache.cxf.transport.servlet.CXFServlet</servlet-class>
		<load-on-startup>1</load-on-startup>
	</servlet>

	<servlet-mapping>
		<servlet-name>CXFServlet</servlet-name>
		<url-pattern>/services/*</url-pattern>
	</servlet-mapping>
	<!-- end CXF -->
</web-app>
```

在web.xml中，

``` xml
<context-param>
	<param-name>contextConfigLocation</param-name>
	<param-value>/WEB-INF/*-context.xml</param-value>
</context-param>
<listener>
	<listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
</listener>
```
这是最基本的声明Spring的方式。在这个例子中，我们使用了通配符`/WEB-INF/*-context.xml`来加载我们所需要的spring配置文件。  
你可以按照通配符的格式定义不同的Spring配置文件，方便管理。

``` xml
<servlet>
	<servlet-name>CXFServlet</servlet-name>
	<servlet-class>org.apache.cxf.transport.servlet.CXFServlet</servlet-class>
	<load-on-startup>1</load-on-startup>
</servlet>
<servlet-mapping>
	<servlet-name>CXFServlet</servlet-name>
	<url-pattern>/services/*</url-pattern>
</servlet-mapping>
```
这一段声明了CXFServlet，用来映射来自/services/*的url，使用REST的方式来处理。

通过这一系列的配置。反过来就可以得到各个REST接口所对应的url路径。

例如，**GET http://localhost:8080/RestDemo/services/rest/UserManager/users/{id}**  
就会调用UserManagerService类的readUser()方法
就可以获取id为{id}的用户的信息。

## step 3. 测试

我们使用Chrome的扩展应用[Advanced Rest Client](https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo)
来模拟HTTP通信和测试。
Advanced Rest Client 界面如下:  

![advanced rest client](http://d.pr/i/khAv+)

在上图中，我们创建一个user用户。  
地址栏填写请求Rest服务的url地址: http://localhost:8080/RestDemo/services/rest/UserManager/users/  
因为是创建用户，下面的请求方法选择POST  
再下面是设置你的请求Header信息，如"Content-Type"，这里我们留空  
接着是payload，我们填写一个josn格式的用户，将会被包含在请求中。  
``` javascript
{"name":"Rocky","email":"someting@nospam.org","birthDate":"1975-01-01","city":"Omaha","state":"CN"}
```
再下面我们选择数据格式为"application/json"。  
然后点击Send。  
下面出现了请求的结果，因为我们服务器端在createUser成功后没有返回，所以REST返回的状态吗是204  
>
>Status Code: 204 - No Content 
>
>The server successfully processed the request, but is not returning any content.

我们再使用GET获取刚刚创建的用户信息(刚刚创建的用户id为1)  

![get user 1](http://d.pr/i/ENhC+)

点击Send之后结果如下：  
![result of user 1](http://d.pr/i/91Pp+)

可以看到返回 200状态  
在返回的结果中，有user 1的信息。  

**注意：** 
我们声明readUser()的时候，返回值是User对象，而为什么这里response返回了josn格式的用户信息呢？    
因为我们使用了JsonProvider。

``` xml
<!-- 创建一个jsonProvider给jaxrs:server元素使用 -->
<bean id="jsonProvider" class="org.codehaus.jackson.jaxrs.JacksonJsonProvider" />

<!-- 暴露我们将要提供的Rest服务 -->
<jaxrs:server id="userManagerREST" address="/rest/UserManager">
	<jaxrs:serviceBeans>
		<ref bean="userManagerService" />
	</jaxrs:serviceBeans>
	<jaxrs:providers>
		<ref bean='jsonProvider' />
	</jaxrs:providers>
</jaxrs:server>
```
jsonProvider自动将请求中json格式的User参数，变为User对象，传递给createUser(User user)作为参数。  
而将User readUser()的结果转化成json格式响应给客户端。。


