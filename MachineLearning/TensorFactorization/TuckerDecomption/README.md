# Tucker Decomption:High Oder SVD
Tucker分解：高階特異値分解
* 高階テンソルに対するテンソル因子分解
* 本プログラムは3階テンソルに対するテンソル因子分解を行う

## param.py

### init(User,Item,Cotext)
引数で指定して基礎データの取得を行う
* User:ユーザー数
* Item:アイテム数
* Cotext:コンテキスト数

### get_sample()
ランダムで評価値3階テンソルを取得する

### tensor_diplay
3階テンソルを表示する

## tensor.py

### unfolding(data,mode)
3階テンソルの各モード展開を行う
* data:param.pyによって取得したパラメーター
* mode:展開したいモードの指定

### svd(matrix)
引数の行列に対して特異値分解を行う
* matrix:特異値分解を行う行列
* return:特異値分解で取得した左特異行列

### core_calc(data)
コアテンソルを計算する

### RMSE(data)
二乗平均平方根誤差を計算する

## test.py
テスト用プログラム
