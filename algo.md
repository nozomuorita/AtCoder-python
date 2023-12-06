<h1>概要</h1>
Status: 初めて解いたときの状況<br>
体感難易度: 1~10の10段階(大雑把に解いた時の自分の感覚で評価)、適宜更新<br>
<ul>
	<li>1: 脳死</li>
	<li>2: 問題を見て解法(方針)が浮かび、実装も苦ではなかったとき</li>
	<li>3: まあ、実装(AC)はできるかな程度(想定解とあってるかは考慮しない)</li>
	<li>4: 解法は浮かんだが、実装(の仕方)に少し苦労</li>
	<li>5: 使うアルゴリズムや方針を言われたら「あ～」となる(わかる)</li>
	<li>6: 解説を読んだら理解できて、自力実装できる</li>
	<li>7: 解説見てやることはわかったが実装に苦労</li>
	<li>8: 解説や他者コードを見ながらもがいたらほわっとだけ理解できたかな？って感じ</li>
	<li>9: 解説、他者ACコードを見てもさっぱり</li>
	<li>10: もはや問題文の意味がわからん</li>
</ul>

<h1>目次</h1>
※各表はDiff順
<h2><a href="#brute-force">全探索</a></h2>
<ul>
	<li><a href="#bit-brute">bit全探索</a></li>
</ul>

<h2><a href="#dp">DP</a></h2>
<ul>
	<li><a href="#dp-basic">基礎</a></li>
	<li><a href="#dp-count">数え上げ</a></li>
</ul>

<h2><a href="#graph">グラフ系</a></h2>

<h2><a href="#consideration">考察系(テクニック)</a></h2>

<h2><a href="#math">数学的問題</a></h2>
<ul>
	<li><a href="#prime">素数</a></li>
	<li><a href="#yakusu">約数</a></li>
	<li><a href="#math-other">その他</a></li>
</ul>

<h2><a href="#others">その他</a></h2>
<ul>
	<li><a href="#run-length-encoding">ランレングス圧縮</a></li>
	<li><a href="#merge-tech">マージテク</a></li>
	<li><a href="#imos">いもす法</a></li>
	<li><a href="#string">文字列操作</a></li>
	<ul>
		<li><a href="#kakko">カッコ列系</a></li>
		<li><a href="#rotate">回文系</a></li>
		<li><a href="#string-other">その他</a></li>
	</ul>
	<li><a href="#dict">辞書順系</a></li>
	<li><a href="#multiset">multiset</a></li>
	<li><a href="#mex">MEX</a></li>
	<li><a href="#topological">トポロジカルソート</a></li>
</ul>





<h1 id="brute-force">全探索</h1>

|Problem|Diff|Problem name|Status|体感難易度|最終提出日|
|:----:|:----:|:----:|:----:|:----:|:----:|
|<a href="https://atcoder.jp/contests/abc330/tasks/abc330_c">ABC330 C</a>|519|Minimize Abs 2|まあAC|4|2023-11-25
|<a href="https://atcoder.jp/contests/abc189/tasks/abc189_c">ABC189 C</a>|565|Mandarin Orange|方針を見てAC|5|2023-11-21

<h2 id="bit-brute">bit全探索</h2>

|Problem|Diff|Problem name|Status|体感難易度|最終提出日|
|:----:|:----:|:----:|:----:|:----:|:----:|
|<a href="https://atcoder.jp/contests/abc289/tasks/abc289_c">ABC289 C</a>|396|Coverage|一発自力AC|3|2023-11-28


<h1 id="dp">DP</h1>
<h2 id="dp-basic">基礎</h2>

|Problem|Diff|Problem name|Status|体感難易度|最終提出日|
|:----:|:----:|:----:|:----:|:----:|:----:|
|<a href="https://atcoder.jp/contests/abc289/tasks/abc289_d">ABC289 D</a>|551|Step Up Robot|一発自力AC|3|2023-11-28
|<a href="https://atcoder.jp/contests/abc286/tasks/abc286_d">ABC286 D</a>|607|Money in Hand|一発自力AC|2|2023-11-24
|<a href="https://atcoder.jp/contests/abc266/tasks/abc266_d">ABC266 D</a>|840|Snuke Panic (1D)|一発自力AC|3|2023-11-25
|<a href="https://atcoder.jp/contests/abc271/tasks/abc271_d">ABC271 D</a>|886|Flip and Adjust|一発自力AC|3|2023-12-04

<h2 id="dp-count">数え上げ</h2>

|Problem|Diff|Problem name|Status|体感難易度|最終提出日|
|:----:|:----:|:----:|:----:|:----:|:----:|
|<a href="https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_c">三井住友信託銀行プログラミングコンテスト2019 C</a>|253|100 to 105|方針を見てAC|5|2023-11-21
|<a href="https://atcoder.jp/contests/abc291/tasks/abc291_d">ABC291 D</a>|720|Flip Cards|一発自力AC|2|2023-11-30
|<a href="https://atcoder.jp/contests/abc189/tasks/abc189_d">ABC189 D</a>|769|Logical Expression|一発自力AC|2|2023-11-21

<h1 id="graph">グラフ系</h1>

|Problem|Diff|Problem name|Status|体感難易度|最終提出日|
|:----:|:----:|:----:|:----:|:----:|:----:|
|<a href="https://atcoder.jp/contests/abc284/tasks/abc284_c">ABC284 C</a>|193|Count Connected Components|一発自力AC|2|2023-11-22
|<a href="https://atcoder.jp/contests/abc289/tasks/abc289_b">ABC289 B</a>|225|レ|一発自力AC|3|2023-11-28
|<a href="https://atcoder.jp/contests/abc288/tasks/abc288_c">ABC288 C</a>|436|Don’t be cycle|一発自力AC|2|2023-11-24
|<a href="https://atcoder.jp/contests/abc287/tasks/abc287_c">ABC287 C</a>|466|Path Graph?|一発自力AC|2|2023-11-24
|<a href="https://atcoder.jp/contests/abc292/tasks/abc292_d">ABC292 D</a>|579|Unicyclic Components|一発自力AC|3|2023-12-01
|<a href="https://atcoder.jp/contests/abc285/tasks/abc285_d">ABC285 D</a>|663|Change Usernames|なんとかAC|4|2023-11-22
|<a href="https://atcoder.jp/contests/abc079/tasks/abc079_d">ABC079 D</a>|949|Grid Repainting|解説見てAC|6|2023-12-05
|<a href="https://atcoder.jp/contests/abc088/tasks/abc088_d">ABC088 D</a>|999|Grid Repainting|自力一発AC|4|2023-12-03
|<a href="https://atcoder.jp/contests/abc284/tasks/abc284_e">ABC284 E</a>|1043|Count Simple Paths|なんとかAC|4|2023-11-23
|<a href="https://atcoder.jp/contests/abc075/tasks/abc075_d">ABC075 d</a>|1067|Bridge|自力一発AC|3|2023-11-27
|<a href="https://atcoder.jp/contests/abc286/tasks/abc286_e">ABC286 E</a>|1128|Souvenir|なんとかAC|4|2023-11-24
|<a href="https://atcoder.jp/contests/abc328/tasks/abc328_e">ABC328 E</a>|1160|Modulo MST|他者コード見てAC|6|2023-12-06
|<a href="https://atcoder.jp/contests/abc299/tasks/abc299_e">ABC299 E</a>|1262|Nearest Black Vertex|解説見てAC|6|2023-12-03
|<a href="https://atcoder.jp/contests/abc292/tasks/abc292_e">ABC292 E</a>|1272|Transitivity|解説見てAC|6|2023-12-01
|<a href="https://atcoder.jp/contests/abc289/tasks/abc289_e">ABC289 E</a>|1318|Swap Places|解説見てAC|6|2023-11-29


<h1 id="consideration">考察系(テクニック)</h1>

|Problem|Diff|Problem name|Status|体感難易度|最終提出日|
|:----:|:----:|:----:|:----:|:----:|:----:|
|<a href="https://atcoder.jp/contests/abc290/tasks/abc290_c">ABC290 C</a>|225|Max MEX|解説見てAC|7|2023-11-28
|<a href="https://atcoder.jp/contests/abc175/tasks/abc175_c">ABC175 C</a>|417|Walking Takahashi|自力一発AC|3|2023-11-27
|<a href="https://atcoder.jp/contests/abc330/tasks/abc330_d">ABC330 D</a>|569|Counting Ls|解説見てAC|4|2023-11-26
|<a href="https://atcoder.jp/contests/abc287/tasks/abc287_d">ABC287 D</a>|796|Match or Not|自力AC|2|2023-11-24
|<a href="https://atcoder.jp/contests/abc290/tasks/abc290_d">ABC290 D</a>|1036|Marking|解説見てAC|7|2023-11-28
|<a href="https://atcoder.jp/contests/abc287/tasks/abc287_e">ABC287 E</a>|1093|Karuta|解説見てAC|5|2023-11-24
|<a href="https://atcoder.jp/contests/abc046/tasks/abc046_b">ABC046 B</a>|1260|石取り大作戦|解説見てAC|7|2023-11-28
|<a href="https://atcoder.jp/contests/abc169/tasks/abc169_e">ABC169 E</a>|1353|Karuta|解説見てAC|7|2023-11-27
|<a href="https://atcoder.jp/contests/abc329/tasks/abc329_e">ABC329 E</a>|1539|Stamp|解説見てなんとかAC|7|2023-11-21


<h1 id="math">数学的問題</h1>
<h2 id="prime">素数</h2>

|Problem|Diff|Problem name|Status|体感難易度|最終提出日|
|:----:|:----:|:----:|:----:|:----:|:----:|
|<a href="https://atcoder.jp/contests/abc284/tasks/abc284_d">ABC284 D</a>|658|Happy New Year 2023|解説見てAC|6|2023-11-22
|<a href="https://atcoder.jp/contests/abc096/tasks/abc096_d">ABC096 D</a>|1226|Five, Five Everywhere|解説見てAC|6|2023-12-06

<h2 id="yakusu">約数</h2>

|Problem|Diff|Problem name|Status|体感難易度|最終提出日|
|:----:|:----:|:----:|:----:|:----:|:----:|
|<a href="https://atcoder.jp/contests/abc292/tasks/abc292_c">ABC292 C</a>|444|Four Variables|なんとかAC|5|2023-12-01

<h2 id="math-other">その他</h2>

|Problem|Diff|Problem name|Status|体感難易度|最終提出日|
|:----:|:----:|:----:|:----:|:----:|:----:|
|<a href="https://atcoder.jp/contests/abc330/tasks/abc330_c">ABC330 C</a>|519|Minimize Abs 2|まあAC|4|2023-11-25
|<a href="https://atcoder.jp/contests/typical90/tasks/typical90_cg">競プロ典型-085</a>|-|Multiplication 085|自力AC|4|2023-12-04



<h1 id="others">その他</h1>
<h2 id="run-length-encoding">ランレングス圧縮</h2>

|Problem|Diff|Problem name|Status|体感難易度|最終提出日|
|:----:|:----:|:----:|:----:|:----:|:----:|
|<a href="https://atcoder.jp/contests/abc329/tasks/abc329_c">ABC329 C</a>|205|Count xxx|コンテスト自力AC|3|2023-11-21

<h2 id="merge-tech">マージテク</h2>

|Problem|Diff|Problem name|Status|体感難易度|最終提出日|
|:----:|:----:|:----:|:----:|:----:|:----:|
|<a href="https://atcoder.jp/contests/abc329/tasks/abc329_f">ABC329 F</a>|1207|Colored Ball|解説見てAC|5|2023-11-21

<h2 id="imos">いもす法</h2>

|Problem|Diff|Problem name|Status|体感難易度|最終提出日|
|:----:|:----:|:----:|:----:|:----:|:----:|
|<a href="https://atcoder.jp/contests/abc221/tasks/abc221_d">ABC221 D</a>|832|Online games|自力一発AC|2|2023-11-22
|<a href="https://atcoder.jp/contests/abc278/tasks/abc278_e">ABC278 E</a>|996|Grid Filling|解説見てAC|7|2023-12-01
|<a href="https://atcoder.jp/contests/typical90/tasks/typical90_ab">競プロ典型-028</a>|-|Cluttered Paper|解説見てAC|7|2023-12-01

<h2 id="string">文字列操作</h2>
<h3 id="kakko">カッコ列系</h3>

|Problem|Diff|Problem name|Status|体感難易度|最終提出日|
|:----:|:----:|:----:|:----:|:----:|:----:|
|<a href="https://atcoder.jp/contests/abc283/tasks/abc283_d">ABC283 D</a>|453|Scope|自力一発AC|3|2023-11-22

<h3 id="rotate">回文系</h3>

|Problem|Diff|Problem name|Status|体感難易度|最終提出日|
|:----:|:----:|:----:|:----:|:----:|:----:|
|<a href="https://atcoder.jp/contests/abc286/tasks/abc286_c">ABC286 C</a>|565|Rotate and Palindrome|自力一発AC|2|2023-11-24

<h3 id="string-other">その他</h3>

|Problem|Diff|Problem name|Status|体感難易度|最終提出日|
|:----:|:----:|:----:|:----:|:----:|:----:|
|<a href="https://atcoder.jp/contests/abc287/tasks/abc287_d">ABC287 D</a>|796|Match or Not|自力AC|2|2023-11-24


<h2 id="dict">辞書順系</h2>

|Problem|Diff|Problem name|Status|体感難易度|最終提出日|
|:----:|:----:|:----:|:----:|:----:|:----:|
|<a href="https://atcoder.jp/contests/abc285/tasks/abc285_c">ABC285 C</a>|157|abc285_brutmhyhiizp|自力一発AC|2|2023-11-23

<h2 id="multiset">multiset</h2>

|Problem|Diff|Problem name|Status|体感難易度|最終提出日|
|:----:|:----:|:----:|:----:|:----:|:----:|
|<a href="https://atcoder.jp/contests/abc330/tasks/abc330_e">ABC330 E</a>|1004|Mex and Update|自力なんとかAC|4|2023-11-25

<h2 id="mex">MEX</h2>

|Problem|Diff|Problem name|Status|体感難易度|最終提出日|
|:----:|:----:|:----:|:----:|:----:|:----:|
|<a href="https://atcoder.jp/contests/abc290/tasks/abc290_c">ABC290 C</a>|225|Max MEX|解説見てAC|7|2023-11-28
|<a href="https://atcoder.jp/contests/abc330/tasks/abc330_e">ABC330 E</a>|1004|Mex and Update|自力なんとかAC|4|2023-11-25

<h2 id="topological">トポロジカルソート</h2>

|Problem|Diff|Problem name|Status|体感難易度|最終提出日|
|:----:|:----:|:----:|:----:|:----:|:----:|
|<a href="https://atcoder.jp/contests/abc291/tasks/abc291_e">ABC291 E</a>|1069|Find Permutation|解説見てAC|7|2023-11-30





<h1>その他 超超超典型基礎問題</h1>
各アルゴリズムの最も基本となる問題
<h2>グラフアルゴリズム</h2>
<ul>
	<li><a href="https://atcoder.jp/contests/abc284/tasks/abc284_c">ABC284 C</a>：連結成分数カウント（単純無向グラフ）→DFS, BFS, UnionFind</li>
	<li><a href="https://atcoder.jp/contests/abc285/tasks/abc285_d">ABC285 D</a>：閉路検出（単純無向グラフ）→DFS, BFS, UnionFind</li>
	<li><a href="https://atcoder.jp/contests/abc287/tasks/abc287_c">ABC287 C</a>：パスグラフ判定（単純無向グラフ）→DFS, BFS, UnionFind</li>
	<li><a href="https://atcoder.jp/contests/abc287/tasks/abc287_c">ABC288 C</a>：閉路数カウント（単純無向グラフ）→DFS, BFS, UnionFind</li>
	<li><a href="https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_e">全点対最短経路問題</a>：ワーシャルフロイド</li>
	<li><a href="https://atcoder.jp/contests/abc079/tasks/abc079_d">ABC079 D</a>：ワーシャルフロイド</li>
</ul>
<h2>DP</h2>
<ul>
	<li><a href="https://atcoder.jp/contests/abc286/tasks/abc286_d">ABC286 D</a>：基礎DP（コイン問題）</li>
	<li><a href="https://atcoder.jp/contests/abc289/tasks/abc289_d">ABC289 D</a>：基礎DP（階段問題）</li>
</ul>
