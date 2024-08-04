# 工作分配 Discord Bot

### 指令
- /add
- /publish
- /fillout
- /sort

#### 這個專案學習的
- 實現一點點模組化 
- 讓檔案看起來有結構

## sort

### 思考過程

#### 前言
我一開始完全沒有想法，但我連這個作法的名字要叫什麼都不知道（多志願排序？？）導致我也不知道該搜尋什麼，於是我先問了GPT但他似乎沒有理解我的需求，所以我又問了朋友。



<details>
<summary> 嘗試階段 </summary>

### 朋友告訴我就`一輪一輪看，如果前一輪沒選中他，下一輪就讓他有優先選擇權`，一開始還沒聽懂，但懂了後就開始實做了!

### 問題 : 有人工作很多/有人沒工作
#### 因為是照志願看的，雖然可能都是他想做的工作，但有機率會讓他的工作變超多，讓其他人沒工作
##### 解法一 GPT❌:
```py
#根據每人已獲得的工作數量排序，優先選擇工作數少的人
people_names.sort(key=lambda name: worker_dict[name])
```
這個的解法雖然能解決大多數情況，但他當輪志願如果還是滿人了，他還是有機會沒工作

##### 解法二 MOM✅:
發現邏輯會產生問題，提供成功版本的想法
</details>

<details>
<summary> 成功版本  </summary>

### 改變每一輪的定義，`每一輪每個人都一定會拿到一個工作`，假設我這個志願的工作滿人了，不是換下一個人，而是換成我的下一個志願

#### 中間用到的break multiple loops :
https://stackoverflow.com/questions/189645/how-can-i-break-out-of-multiple-loops

</details>
