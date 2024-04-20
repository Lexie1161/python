<!doctype html>
<html lang="zh-CN">

	<head>
		<meta charset="utf-8">
		<title>今天吃什么0_o</title>
		<style>
			h1{
				color:darkblue;
				font-size:35px;
			}
			.p{
				color:hotpink;
			}
			h1+from{
				color:darkslateblue;
			}
			tr th{
				color:darkslateblue;
				font-size:20px;
			}
			tr td{
				font-size:15px;
			}
			#fengefu{
				display:none;
			}
			.fengefu2{
				visibility: hidden;
				font-size:1px;
			}
		</style>
	</head>
	<body>
		<h1>用户信息</h1> 
		<from action="/url" method="post">
			姓名：<input name="username" type="text"><br><br>
			体重：<input name="weight" type="text"><br><br>
			身高：<input name="highr" type="text"><br><br>
			性别：女<input name="gender" type="radio" value="female">
			男<input name="gender" type="radio" value="male">
		</from>
		<h2 id="fengefu">----分隔符----</h2>
		<h1>食物选择</h1>
		<table border="6">
			<tr >
				<th bgcolor="yellow">主食</th>
				<th bgcolor="yellow">饮品</th>
				<th bgcolor="yellow">甜点</th>
			</tr>
			<tr>
				<td align="center">盐焗鸡腿饭</td>
				<td align="center">冬瓜茶</td>
				<td class="p" align="center">双皮奶</td>
			</tr>
			<tr>
				<td align="center">黑椒牛柳意面</td>
				<td align="center">玫瑰柠檬茶</td>
				<td class="p" align="center">冰淇淋</td>
			</tr>
			<tr>
				<td align="center">披萨</td>
				<td align="center">可乐</td>
				<td class="p" align="center">马卡龙</td>
			</tr>
		</table><br>
		<h2 class="fengefu2">====又一分隔符====</h2>
		<iframe src="D:\数据采集\练习\名言.html" widtn="6"></iframe>
	</body>
</html>