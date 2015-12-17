# SingularValueDecomption
* 特異値分解

## parameter.py
### __init__(User,Item,K)
* 引数で指定して、基礎データを取得する
* User:ユーザー数
* Item:アイテム数
* K:特徴量数

### get_sumple()
* ランダムで評価値行列を取得する

## svd.py
### __init__(gamma,lamda)
* 引数で指定して、lamda,gammaの値を取得
* gamma:学習率
* lamda:正則化パラメーター

### iteration(data,iteration)
* 引数でiteration数を指定して、learn()で学習を実行する
* data:paramter.pyによって取得しパラメーター
* iteration:イテレーション回数(test.pyでは2000回)

### learn(data)
* 評価値行列との誤差を使ってユーザーバイアス、アイテムバイアス、ユーザー行列、アイテム行列を更新する
* data:paramter.pyによって取得したパラメーター

### error(data,all)
* 評価値行列とユーザー行列とアイテム行列を再構築した行列の1セルの誤差を求める
* data:paramter.pyによって取得したパラメーター
* all:全ユーザーの平均評価値

### total_error(data)
* 全体誤差が減少しているかを確認する

## test.py
* テスト用プログラム

