# 工作分配 Discord Bot

### 指令
- /add
- /publish
- /fillout
- /sort

#### 專案目標:實現一點點模組化

## sort

### 思考過程

#### 前言
我一開始完全沒有想法人，但我連這個作法的名字要叫什麼都不知道（多志願排序？？）導致我也不知道該搜尋什麼，於是我先問了GPT但他似乎沒有理解我的需求，所以我又問了朋友。



<details>
<summary> 版本一 </summary>
<br>

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
發現邏輯會產生問題，所以就有了版本二
</details>

<details>
<summary> 版本二 </summary>
<br>


</details>
