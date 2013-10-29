<h1 class="wmd-title" id="oracle中的时间日期处理">ORACLE中的时间日期处理</h1>

<p>oracle中有一个当前时间的值<strong><code>sysdate</code></strong></p>

<blockquote>
  <p>select sysdate from dual</p>
  
  <table>
<thead>
<tr>
  <th>SYSDATE</th>
</tr>
</thead>
<tbody><tr>
  <td>2013/10/25 11:18:36</td>
</tr>
</tbody></table>

</blockquote>

<p>例如我们现在有一张表BLOG表</p>

<table>
<thead>
<tr>
  <th>blogid</th>
  <th>blogtitle</th>
  <th>blogauthor</th>
  <th>createtime</th>
</tr>
</thead>
<tbody><tr>
  <td>10000</td>
  <td>博客一</td>
  <td>作者一</td>
  <td>2013/10/25 10:10:10</td>
</tr>
</tbody></table>


<p>想要查看今天创建的博客应该使用</p>

<pre><code>select * from blog where createtime = sysdate #错误，这样比较加入了时分秒的比较，可能得不到任何结果
</code></pre>

<hr>

<h3 class="wmd-title" id="trunc函数"><strong><code>trunc()</code></strong>函数</h3>

<p>trunc()函数语法</p>

<blockquote>
  <p>trunc(date[,fmt]) <br>
  将根据fmt参数对date进行截取，如果没有fmt参数，将返回离date最近的日期信息（去掉时分秒）</p>
</blockquote>

<p>所以要查看所有今天创建的博客应该使用下面的SQL语句</p>

<pre class="prettyprint prettyprinted" style=""><code class="language- sql"><span class="pln">    </span><span class="kwd">select</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> </span><span class="kwd">from</span><span class="pln"> blog </span><span class="kwd">where</span><span class="pln"> trunc</span><span class="pun">(</span><span class="pln">createtime</span><span class="pun">)</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> trunc</span><span class="pun">(</span><span class="pln">sysdate</span><span class="pun">)</span><span class="pln">
    </span><span class="com">#or</span><span class="pln">
    </span><span class="kwd">select</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> </span><span class="kwd">from</span><span class="pln"> blog </span><span class="kwd">where</span><span class="pln"> createtime </span><span class="pun">&gt;</span><span class="pln"> trunc</span><span class="pun">(</span><span class="pln">sysdate</span><span class="pun">)</span></code></pre>

<pre><code>
</code></pre>