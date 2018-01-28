# 术语
[comment]: # (XML相关)
URI(Uniform Resource Identifier, 统一资源标志符)
DTD(Document Type Definition, 文档类型定义)
XSD(XML Schema Definition, XML Schema 定义)
XSL(eXtensible Stylesheet Language)
[comment]: # (Webservice相关)
WSDL(Web Services Description Language, 网络服务描述语言)
SOAP(Simple Object Access Protocol, 简单对象访问协议)
# 概述
XML
[comment]: # (XML相关)
DTD(Document Type Definition)和XSD(XML Schema Definition)来定义XML的结构
XSL(eXtensible Stylesheet Language)来描述数据的样式

XPath: 
XQuery
[comment]: # (Webservice相关)
WebS
# DTD语法
```DTD

```
XML中引用DTD：根节点前面添加<!DOCTYPE 根节点名字 SYSTEM "path/to/dtd">
# XSD语法
应使用命名空间xs, 使用`<schema>`作为根结点

```
<?xml version="1.0"?>
<xs:schema  xmlns:xs="http://www.w3.org/2001/XMLSchema"
            targetNamespace="http://www.w3school.com.cn"
            xmlns="http://www.w3school.com.cn"
            elementFormDefault="qualified">

...
...
</xs:schema>
```
## 限定
## 复合元素
XML中引用XSD
根节点添加属性xsi:schemaLocation = "path/to/xsd"
空元素
举例：
```
    <product prodid="1345" />
```
- xs:string
- xs:decimal
- xs:integer
- xs:boolean
- xs:date
- xs:time
# XSL语法


# 题库
XML与树结构互转
## 手写DTD
类别
EMPTY
ANY

- 声明元素
```xml
<!ELEMENT 元素名称 类别>
<!ELEMENT 元素名称 (子元素)>
```
- 声明属性
```xml
<!ATTLIST 元素名称 属性名称 属性类型 默认值>
```


```xml
<!DOCTYPE note [
  <!ELEMENT RootName (ElementName0, ... , ElementNameN)>    <!-- +:一次或多次 *:零次或多次 ?:零次或一次 -->
  <!ELEMENT ElementName0 (#PCDATA)>
  ...
  <!ELEMENT ElementNameN (#PCDATA)>
]>

<!DOCTYPE RootName SYSTEM "path/to/.dtd">
```
## 手写XSD
```
schema
├─ complexType0
├─ ...
├─ complexTypeN
├─ element0
├─ ...
└─ elementN
```

### 可用类型
字符串
| 名字 | 描述 |
| :---: | :---: |
| ENTITIES | 	  |
| ENTITY | 	  |
| ID | 在 XML 中提交 ID 属性的字符串 (仅与 schema 属性一同使用) |
| IDREF | 在 XML 中提交 IDREF 属性的字符串(仅与 schema 属性一同使用) |
| IDREFS language | 包含合法的语言 id 的字符串 |
| Name | 包含合法 XML 名称的字符串 |
| NCName |   |
| NMTOKEN | 在 XML 中提交 NMTOKEN 属性的字符串 (仅与 schema 属性一同使用) |
| NMTOKENS |  |
| normalizedString | 不包含换行符、回车或制表符的字符串 |
| QName |  |
| string | 字符串 |
| token | 不包含换行符、回车或制表符、开头或结尾空格或者多个连续空格的字符串 |

日期
| 名字 | 描述 |
| :---: | :---: |
| date | 定义一个日期值 |
| dateTime | 定义一个日期和时间值 |
| duration | 定义一个时间间隔 |
| gDay | 定义日期的一个部分 - 天 (DD) |
| gMonth | 定义日期的一个部分 - 月 (MM) |
| gMonthDay | 定义日期的一个部分 - 月和天 (MM-DD) |
| gYear | 定义日期的一个部分 - 年 (YYYY) |
| gYearMonth | 定义日期的一个部分 - 年和月 (YYYY-MM) |
| time | 定义一个时间值 |

数值
| 名字 | 描述 |
| :---: | :---: |
| byte | 有正负的 8 位整数 |
| decimal | 十进制数 |
| int | 有正负的 32 位整数 |
| integer | 整数值 |
| long | 有正负的 64 位整数 |
| negativeInteger | 仅包含负值的整数 ( .., -2, -1.) |
| nonNegativeInteger | 仅包含非负值的整数 (0, 1, 2, ..) |
| nonPositiveInteger | 仅包含非正值的整数 (.., -2, -1, 0) |
| positiveInteger | 仅包含正值的整数 (1, 2, ..) |
| short | 有正负的 16 位整数 |
| unsignedLong | 无正负的 64 位整数 |
| unsignedInt | 无正负的 32 位整数 |
| unsignedShort | 无正负的 16 位整数 |
| unsignedByte | 无正负的 8 位整数 |

### 限定
```xml
<restriction>
 <限定标签 value="限定值" />
</restriction>
```
restriction
| 限定 | 描述 |
| :---: | :---: |
| enumeration | 定义可接受值的一个列表 | [comment]: # (通用)
| maxLength | 定义所允许的字符或者列表项目的最大数目。必须大于或等于0。 | [comment]: # (字符串)
| minLength | 定义所允许的字符或者列表项目的最小数目。必须大于或等于0。 |
| length | 定义所允许的字符或者列表项目的精确数目。必须大于或等于0。 |
| pattern | 定义可接受的字符的精确序列。 |
| maxExclusive | 定义数值的上限。所允许的值必须小于此值。 | [comment]: # (数值/日期)
| maxInclusive | 定义数值的上限。所允许的值必须小于或等于此值。 | [comment]: # (数值/日期)
| minExclusive | 定义数值的下限。所允许的值必需大于此值。 | [comment]: # (数值/日期)
| minInclusive | 定义数值的下限。所允许的值必需大于或等于此值。 | [comment]: # (数值/日期)
| fractionDigits | 定义所允许的最大的小数位数。必须大于等于0。 | [comment]: # (数值)
| totalDigits | 定义所允许的阿拉伯数字的精确位数。必须大于0。 | [comment]: # (数值)
| whiteSpace | 定义空白字符（换行、回车、空格以及制表符）的处理方式。 | [comment]: # (字符串)

### 模板
- 仅含元素的类型
    ```xml
    <xs:complexType name="类型">
        <xs:sequence>
            <xs:element name="子元素" type="类型"/>
            <xs:element name="子元素" type="类型"/>
        </xs:sequence>
    </xs:complexType>
    ```
- 仅含文本的类型
    ```xml
    <xs:complexType name="shoetype">
        <xs:simpleContent>
            <xs:extension base="xs:integer">
                <xs:attribute name="country" type="xs:string" />
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
    ```
- 空元素类型
    ```xml
    <xs:complexType name="类型">
        <xs:attribute name="属性名" type="类型"/>
    </xs:complexType>
    ```
- 混合元素类型: 将`complexType`的`mixed`属性设为`true`，从而支持文本元素穿插
    ```xml
    <xs:complexType mixed="true">
        <xs:sequence>
            <xs:element name="name" type="xs:string"/>
            <xs:element name="orderid" type="xs:positiveInteger"/>
            <xs:element name="shipdate" type="xs:date"/>
        </xs:sequence>
    </xs:complexType>
    ```
- 限制元素的数量: 使用`element`元素的`minOccurs`和`maxOccurs`属性
    ```xml
    <xs:element name="<ElementName>" type="<ElementType>" minOccurs="0" maxOccurs="5"/>
    ```
- 定义`simpleType`或`complexType`
    ```xml
    <!-- element内定义-->
    <xs:element name="<ElementName>" type="<ElementType>" />
    <!-- 外部引用 -->
    <xs:simpleType name="<ElementType>">
        <xs:restriction base="xs:string">
            <xs:pattern value="[0-9]{6}"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:element name="<ElementName>" type="<ElementType>" />
    ```
- 定义`attribute`
    ```xml
    <!-- element内定义 -->
    <xs:element name="<ElementName>" type="<ElementType>">
        <xs:attribute ref="<AttributeName>" use="required"/>
    </xs:element>
    <!-- 外部引用 -->
    <!-- 定义属性 -->
    <xs:element name="<ElementName>" type="<ElementType>" minOccurs="0" maxOccurs="5"/>

    <!-- 引用属性 -->
    <xs:element name="<ElementName>" type="<ElementType>">
        <xs:attribute ref="<AttributeName>" use="required"/>
    </xs:element>
    ```
## XPath
轴和绝对路径的转换

绝对路径起始于正斜杠( / )，而相对路径不会这样。
相对路径
```xpath
step/step/...
```
绝对路径
```xpath
/step/step/...
```
```xpath
轴::结点
```
其中step可以是结点，也可以是轴::结点

| 轴 | 描述 |
| :---: | :---: |
| ancestor | 选取当前节点的所有先辈（父、祖父等）。 |
| ancestor-or-self | 选取当前节点的所有先辈（父、祖父等）以及当前节点本身。 |
| attribute | 选取当前节点的所有属性。 |
| child | 选取当前节点的所有子元素。 |
| descendant | 选取当前节点的所有后代元素（子、孙等）。 |
| descendant-or-self | 选取当前节点的所有后代元素（子、孙等）以及当前节点本身。 |
| following | 选取文档中当前节点的结束标签之后的所有节点。 |
| namespace | 选取当前节点的所有命名空间节点。 |
| parent | 选取当前节点的父节点。 |
| preceding | 选取文档中当前节点的开始标签之前的所有节点。 |
| preceding-sibling | 选取当前节点之前的所有同级节点。 |
| self | 选取当前节点。 |

## XQuery
FLOWR
```xquery
let $disc := ($price * $discount) div 100

for $x in doc("books.xml")/bookstore/book
where $x/price>30
order by $x/title
return $x/title
```
## 手写XSL

- 定义输出
    ```xml
    <xsl:output method="html" indent="yes"/>
    ```
- 为元素赋予样式(template)
    ```xml
    <xsl:template match="元素的XPath"> <!-- 如果应用到整个文档，用"/" -->
    ...
    </xsl:template>
    ```
- 嵌入变量
    ```xml
    <xsl:value-of select="XPath表达式" />
    ```
- 循环
    ```xml
    <xsl:for-each select="XPath表达式">
    ...
    </xsl:for-each>
    ```
- 分支
    - 可以用`<xsl:if>`来选择性输出
        ```xml
        <xsl:if test="表达式">
        ...
        ...如果条件成立则输出...
        ...
        </xsl:if>
        ```
    - 也可以用`<xsl:choose>`设置多个分支结构
        ```xml
        <xsl:choose>
        <xsl:when test="表达式">
            ... 输出 ...
        </xsl:when>
        <xsl:otherwise>
            ... 输出 ....
        </xsl:otherwise>
        </xsl:choose>
        ```
- 排序
    ```xml
    <xsl:sort select="子元素名称" />
    ```

## 手写WSDL
types
- message:  WebService使用的消息
part
operation
portType
binding
port
service
```
definitions [xmlns:wsu, xmlns:wsp, xmlns:wsp1_2, xmlns:wsam, xmlns:soap, xmlns:tns, xmlns:xsd, xmlns, targetNamespace, name]
├─ types
|   └─ xsd:schema
|       └─ xsd:import [namespace, schemaLocation]
├─ message [name]
|   └─ part [name, element="tns:..."]
├─ portType
|   └─ operation [name]
|       ├─ input [wsam:Action, message="messageName"]
|       └─ output [wsam:Action, message="messageName"]
├─ binding
|   ├─ soap:binding [transport, style]
|   └─ operation
|       ├─ input [wsam:Action, message]
|       └─ output [wsam:Action, message]
└─ service [name]
    └─ port [name, binding]
        └─ soap:address [location]
```

## 手写SOAP
```
Envelope
├─ Header
└─ Body
    ├─ <ServiceName>            # Request结构
    |   ├─ <ArgName0>
    |   ├─  ...
    |   └─ <ArgNameN>
    |
    └─ <ServiceName>Response    # Response结构
```




# 命名空间
- xsd
    ```xml
    <xs:schema 
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    targetNamespace="http://www.w3school.com.cn"
    xmlns="http://www.w3school.com.cn"
    elementFormDefault="qualified">
    ```
- xsl
    ```xml
    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    ```
- soap
    ```xml
    <soap:Envelope
    xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
    soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">
    ```
- wsdl
    ```xml
    <definitions 
    xmlns:wsam="http://www.w3.org/2007/05/addressing/metadata" 
    xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
    xmlns:tns="http://provider/" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns="http://schemas.xmlsoap.org/wsdl/"
    targetNamespace="http://provider/"
    name="StringServiceService">
    ```