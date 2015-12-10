# Abstract  
* データセットの加工用プログラム  
* 形式：[UserID,ItemID,Rating,Timestampe]

## DataProcess.py  
* ユーザーの出現回数を指定してデータセットからその出現回数以上のユーザーを抽出する
* 出力：learning(ユーザー数).csv
## DataTimesort.py  
* DataProcoess.pyで作成した学習データに対して、ユーザー毎でTimestampe順にデータを並べ替える
* 出力：learning(ユーザー数)sort.csv
## Dataconstant.py  
* DataTimesort.pyでソートした学習データに対して、時刻t+1に評価したアイテムと時刻tに評価したアイテムを比較し、指定した時間内に継続してアイテムを評価しているかを判断する
* 出力：learning(ユーザー数)con.csv
