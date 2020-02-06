### 进阶使用Selenium

#### 定位UI元素的方式

~~~markdown
WebElements
~~~

##### find_element和find_elements的区别

~~~markdown
element:获取一个标签，如果有多个，只获取第一个。
elements:获取多个标签。
~~~

##### find_element_by_id()

~~~markdown
根据标签的id，获取当前标签
因为id唯一，所以不区分element和elements的区别
~~~

##### find_elements_by_class_name()

~~~markdown
根据标签的class获取当前的标签
因为有相同class的标签可以有多个，所以需要区分element和elements的区别。
~~~

##### find_element_by_link_text(self, link_text)

~~~markdown
获取到具有链接的标签（a标签），标签中的内容为link_text的那个标签。
~~~

##### find_elements_by_xpath(self, xpath)

~~~~markdown
利用xpath规则，从渲染出的页面中获取到某个标签
~~~~

##### find_element_by_name(self, name)

~~~markdown
从渲染中的页面中，选出标签的name属性为name值的标签。
name需要区分element和elements
~~~

##### find_elements_by_css_selector(self, css_selector)

~~~markdown
利用CSS选择器，去选择出某个标签。（CSS选择器详见侯老师笔记）
需要区分element和elements的区别
~~~

#### 鼠标动作链

~~~markdown
有时候，我们需要在页面上进行一系列操作，比如：点击滑块（鼠标左键的单击），移动滑块（按住左键移动），松开鼠标（松开鼠标左键）
~~~

- Action Chains

![Action_chains](E:\Python186共享文件夹\第三阶段\笔记\pic\Action_chains.png)

#### 弹窗处理

~~~markdown
当触发了alert弹窗之后
driver.switch_to.alert()
~~~

#### 页面切换

~~~markdown
driver.switch_to.window(name)
~~~

#### 页面的前进和后退

~~~markdown
driver.forward()
driver.back()
~~~

