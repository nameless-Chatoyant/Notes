# 概述
好应用有以下三个特点
可扩展性、可靠性、高性能
J2EE应用的特点：
分布式(distributed)
多层(multi-tier)
组件&容器架构



# 展示层Components
## Servlet
Servlet在实现View的方面是比较羸弱的，使用`PrintWriter`对象，调用其`println()`方法，为response增加一行数据。
## JSP
Java Server Pages, Java服务器页面
JSP是更偏向于View的组件，有点像写template

# 业务逻辑层Components
业务逻辑，就是根据业务要实现在某一特定状态下的对应规则。
## EJB
EJB是Java建立分布式业务逻辑的标准。
分为三种：Session Bean, Entity Bean和Message-Driven Bean

### Entity Bean
表示了业务数据。
Entity Bean不是Model而是业务数据。
实体是对数据项的封装，需要有与关系型数据库中的关系的**双向映射**
持久化的

Entity Bean分两种，取决于对DB的操作是Container提供还是Bean提供
- CMP(Container-Managed Persistent) Entity Bean
- BMP(Bean-Managed Persistent) Entity Bean

对比
CMP比BMP开发速度快

### Session Bean
表示了业务处理。MVC中的C
- Stateless Session Bean: 构造函数不接收客户端信息，所有实例都相同
- Stateful Session Bean: 构造函数接收客户端信息，每一个实例不同
对于Stateless Session Bean，因为其所有实例都相同，所以可以用pooling的方法。
### Message-Driven Bean
Entity Bean和Session Bean都在用同步编程模型，客户端向EJB发请求，然后进入业务逻辑。
MDB引入了异步编程模型，

MDB与JMS的关系
- MDB是JMS消息的消费者
- JMS是MDB的客户端
- MDB让EJB和JMS一体化

# 服务
## JNDI
Java Naming & Directory Interface, Java命名和目录接口

为了进一步解耦这些组件，JNDI
有一个中心记录
例子：全班同学的联系方式都保存在班长那里，当一位同学需要更换自己的联系方式，他只需要通知班长。而每位同学需要联系其他同学时，只需从班长这里获得那位同学的联系方式。与之相反的情况，每个同学都保存着其他所有同学的联系方式，每改一个同学的联系方式，所有人的通讯录都要改。

import `javax.naming`包
```java
Context ctx = new InitialContext();
```
`Context`对象
- `Object lookup(Name name)`: 返回`name`对应的Object，要做强制类型转换
- `void bind(Name name, Object obj)`: 绑定
- `void rebind(Name name, Object obj)`: 重绑定
- `void unbind(Name name)`: 解绑
## JDBC

JDBC是Java访问数据库的标准，使用JDBC可以编写不依赖于特定数据库的代码，更换数据库只需要更换driver就好了。
分两种：直接建立connection，或是从connection pool中得到connection
直接建立connection的缺点
每一处使用connection

1. 每次访问数据库都建立新的连接，要付出很大的代价。
2. 和DBMS相关的细节不应该硬编码到客户端代码里，建立连接需要DB地址、用户名、密码，这些东西留在客户端是非常危险的。
3. 与DBMS解耦，比如说更换了数据库的实现，不用更新客户端代码。
4. 限制connection的数量可以提高DBMS的效率。

DataSource用JNDI bind

`javax.sql.DataSource`接口
```java
Context ctx = new InitialContext();
DataSource ds = (DataSource)ctx.lookup("NameOfDataSource");
Connection conn = ds.getConnection();
Statement stmt = conn.createStatement();
ResultSet rs = stmt.execute("do something");

// 依次关闭
rs.close();
stmt.close();
conn.close();
```

业务逻辑层调用JDBC是非持久化的，
## JTA
Java Transaction API, Java事务API
相关包: `javax.transaction`

事务: 对数据库的一系列操作从逻辑上可以看成整体的一个操作，如清购物车，涉及到检查余额、减少商品数量、减少RMB等，这个就叫事务。
数据库的ACID原则
- 原子性(Atomicity): 每个事务中的所有操作要么全部完成，要么就像全部没有发生一样。
- 一致性(Consistency): 任何事务都会使数据库从一种合法的状态变为另一种合法的状态。
- 隔离性(Isolation): 并发和串行化执行多个事务对系统的状态的影响是一样的。 
- 持久性(Durability): 事务提交后，其状态就保持不变。
为满足

```java
// import
import javax.transaction.UserTransaction;

Context ctx = new InitialContext();
UserTransaction tx = (UserTransaction)ctx.lookup("NameOfUserTransaction");
tx.begin();
DataSource ds = (DataSource)ctx.lookup("NameOfDataSource");
Connection conn = ds.getConnection();
Statement stmt = conn.createStatement();
ResultSet rs = stmt.execute("do something");
tx.commit();

// 依次关闭
rs.close();
stmt.close();
conn.close();
```
`UserTransaction.begin()`和`UserTransaction.commit()`之间对数据库的操作将满足ACID.

## RMI
Remote Method Invocation, 远程方法调用

客户端Stub，公共的Interface定义了可调用的方法
Stub和Skeleton
客户端: 
有点像JNDI
获得一个`Registry`对象，调用其`lookup()`方法得到Stub，强制类型转换成客户端代码中定义的Interface，然后使用。

## JMS
Java Message Service, Java消息服务
`javax.jms`包

JMS可以实现异步地处理客户端请求，从而提高服务器性能。
J2EE架构下，Servlet总是做生产者，而消费者通常是MDB。当在Servlet里调用花费时间较长的方法，整个Servlet就阻塞了，表现就是客户端网页一直转圈圈。
同步流程:jsp → servlet → Session Bean → Entity Bean
异步流程: jsp → servlet → JMS → MDB → Session Bean → Entity Bean

如上所示，消息先传给JMS，再传给MDB，从而实现异步处理消息。
有Queue和Topic两种消息传递模型
点对点是Queue模型
发布／订阅是Topic模型

JMS的实现

### Queue模型
#### 生产者
`QueueConnectionFactory` → 
```java
// JNDI相关
import javax.naming.Context;
import javax.naming.NamingException;
/* JMS相关 */
import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.QueueConnectionFactory;
import javax.jms.QueueSender;   // 生产者的核心
import javax.jms.TextMessage;   // 这里以文本消息为例
import javax.jms.Session;

/* 照例，用ctx.lookup得工厂类，然后建立connection */
QueueConnectionFactory qConFactory = (QueueConnectionFactory)ctx.lookup("<QueueConnectionFactoryName>");
Queue messageQueue = (Queue)ctx.lookup("<MessageQueueName>");
QueueSession session = qCon.createQueueSession(
    false,  // not a transacted session
    Session.AUTO_ACKNOWLEDGE
);
QueueSender sender = session.createSender(messageQueue);
```
#### 消费者
```java
// 引入必要包
import javax.jms.Queue;

QueueConnectionFactory qConFactory = (QueueConnectionFactory)ctx.lookup("<QueueConnectionFactoryName>");
QueueConnection qCon = qConFactory.createQueueConnection();
Queue messageQueue = (Queue)ctx.lookup("<MessageQueueName>");
QueueSession session = qCon.createQueueSession(
    false, // not a transacted session
);

receiver.setMessageListener();

```

### Topic模型
Queue

TODO

## JavaMail
JavaMail为开发者提供了发送E-mail的API，当然E-mail服务器还是得自己建

E-mail相关协议
POP3 (yahoo.ca) IMAP (hotmail)

## JAAS
Java Authentication & Authorization Service, Java验证和授权API

开发应用时这是一个很常见的需求：不同用户的界面（功能）也不一样，没有登录的情况只允许访问特定的页面。
最简单的实现方法是每一段代码里都添加上验证，复用。

验证(Authentication)解决“你是谁？”的问题，授权(Authorization)解决“你被允许做什么？”的问题
授权的实现：给用户分组，给不同的组赋予不同的权限。
Users, 就是对用户的建模
Roles，用户属于哪种角色
Groups，分组
Principals，用来约束一个Group

声明安全性(Declarative Security)与编码安全性(Programmatic Security)是J2EE的两种安全性编程模型

声明安全性采用外置的配置文件，而编码安全性是硬编码到代码里
软硬编码带来的不同。
当声明安全性不足以表达应用的安全性模型时，会采用编码安全性。
当角色和安全信息与数据挂钩，只能通过编码安全性，在程序运行时动态授权。


# SSH Framework
## Struts2
## Spring
## Hibernate
一个对象关系映射框架

持久化，简单来说就是save/load的过程。
数据库的持久化，指将内存中的数据模型转换为存储模型。

# 总结
RMI和JNDI服务帮助建立高扩展性的分布式应用。
分布式依赖于网络，还存在着时间和资源上的耗费。没必要就不要用。


# 流程
- 同步
    - 使用标准: JSP(HTML form) → Servlet → Session Bean → Entity Bean → DB
    - 使用框架: 
- 异步
    - 使用标准: JSP(HTML form) → Servlet → **JMS Queue/Topic → MDB** → Session Bean → Entity Bean → DB
    - 使用框架
