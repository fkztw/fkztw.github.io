Title: zdict 介紹  
Slug: zdict-intro  
Date: 2018-01-18 22:30:24  
Authors: fkz  
Category: Note  
Tags: zdict, online dictionary, cli, 2018 iT 邦幫忙鐵人賽  
Summary: 介紹一下自己和幾個朋友寫的 zdict 這套工具  
Modified: 2018-02-01 00:38:24  
  
  
## TL;DR  
  
[GitHub - zdict/zdict: The last online dictionary framework you need. (?)](https://github.com/zdict/zdict)  
  
---  
  
## 前言  
  
在[我平常在電腦上用了哪些程式 | Just for noting](https://blog.fkz.tw/posts/2018/01/09/tools-i-use/)這篇，有提到會為 `zdict` 這套我和幾個朋友一起開發的線上字典查詢指令做個詳細一點的介紹，也算是幫 `zdict` 加個繁體中文的文章吧。  
  
因為 repo 上面都是用英文，幾個禮拜前遇到有台灣人想幫忙貢獻，對自己的英文不夠有自信，結果最後寄了 email 用中文問我，想說讓這個工具的文件多一點繁體中文的親切感（？  
  
有空會再寫一篇文章講這位貢獻者來信詢問的問題以及我回覆的內容，主要是跟 GitHub 新手如何參與開源專案有關，想說第一次有人因為 `zdict` 寄信給我，機會難得，順便用這個機會拿 `zdict` 來當活教材。有徵得對方同意了，但文章一直還沒寫 XD。  
  
---  
  
## 簡介  
  
<https://github.com/zdict/zdict>  
  
有以下幾個特性：  
  
+ Python 3 撰寫  
    + 2020 年就要拋棄 Python 2 啦，因為是 side project，所以懶得支援 Python 2 了，請大家直接用 Python 3 吧。  
+ 主要用途就是用來查線上字典  
    + 要連網才能使用  
    + 沒有離線模式  
        + 不使用字典檔  
    + 預設會使用資料庫中的快取（可選擇關閉）  
        + 每次的查詢預設都會先檢查有沒有存在使用者的電腦上的 zdict 資料庫，有的話就會直接拿來用。  
        + 所以如果是查詢自己查過的單字的話，是可以在不用連網的情況下使用的。  
+ 字典預設是使用 Yahoo! 奇摩字典的英翻中或中翻英查詢  
    + 有其他線上字典可供選擇：  
        + `moe`: 萌典  
        + `moe-taiwanese`: 萌典台語  
        + `spanish`: 西班牙語  
        + `jisho`: 日語  
        + `yahoo`: 中英查詢  
        + `urban`: Urban Dictionary，用來查英文流行用語，看美劇滿常用的。  
        + `yandex`: 俄語  
+ 預設會有語法上色（可選擇關閉）  
+ 原生支援 macOS, Linux, FreeBSD。可透過 Docker 在 Windows 上執行。  
+ 有一般模式也有互動模式  
    + 互動模式很適合開啟來掛著，遇到有要查單字的時候就可以直接查，不需要再額外打 `zdict xxx`  
  
---  
  
## 緣起  
  
這個 side project 大概是從 2015 年 4 月開始的，一開始只是因為那陣子很常看美劇，所以有查單字的需求，覺得要開網頁動滑鼠很麻煩，所以就找有沒有可以在終端機裏面直接查字典的服務。  
  
當時是找到 [GitHub - chenpc/ydict](https://github.com/chenpc/ydict)，使用一陣子之後遇到 Yahoo! 字典網頁改版，所以有東西壞掉，發了個 PR 回去，結果作者很久沒處理，看起來在忙其他事了。  
  
原本想說自己的 fork 改一改能用就好，但和 iblis 那天可能嗑了太多 Python，不知道發什麼神經覺得乾脆來弄一個可以整合查詢多個線上字典的框架好了。  
  
因為 ydict 基本上就是個 Python 2 的 script 而已，當時就想說要弄一個 Pure Python 3 然後還要符合基本開源專案架構的 side project，所以 zdict 就這樣誕生了。  
  
---  
  
## 使用說明  
  
這個就直接看 [zdict/README.rst](https://github.com/zdict/zdict/blob/master/README.rst) 吧，裡頭的英文敘述沒有很難，就算看不懂其實也可以直接看截圖和 example 使用應該沒啥問題，我就不在這贅述了。這篇文章會比較像是開發心得的紀錄，留個念想（？）  
  
---  
  
## 雜談  
  
其實我還蠻享受這個和幾個朋友單純因為需求而開的 side project，從開始弄這個專案以來基本上沒啥壓力，然後想試一些跟 Python 有關的新東西都可以在這個 side project 嘗試，因為有了基本的開源專案的框架，要測一些東西也很方便，不需要自己再重頭刻一些有的沒的。  
  
例如：  
  
+ 透過 Travis CI 自動發佈新版本到 PyPI  
+ 透過 Docker Cloud 綁定 GitHub 的權限，在有新的 tag 的時候自動 build image，放到 Docker Hub，完成 Docker Image 的 CI。  
    + 這部份的功能原本是用 Docker Hub 做，但用到一半發現 Docker Hub 在這部份很難用，又剛好看到 Docker Cloud，試了一下發現做的比較好，所以就改用 Docker Cloud 了。  
    + 唯一一個被雷到的部份是，如果原先使用 Docker Hub，改用 Docker Cloud 的話，得把原本的 Docker Hub Repo 砍掉，用 Docker Cloud 來建一個新的 Automated build 的 Repo，這部份可能會多花一點時間。  
+ 支援 Docker Image  
+ pytest, coverage 相關的參數設定  
+ 使用 Pipfile  
  
以上這些都是我初次經驗就拿這個專案來試，我覺得滿開心的。雖然快 3 年過去了，好像仍舊沒有成為當初說的框架，要新增新的字典進來我覺得也還不夠簡單，但就順其自然吧。  
  
然後大家也是有啥需求就自己開 issue，然後自己開發。大多數都是「自己的 issue 自己解的狀況」：  
  
+ 有人因為想在 Vim 裏面用，所以直接寫了個 Vim plugin: [GitHub - zdict/zdict.vim: A vim plugin integrate with zdict - the last online dictionary framework you need.](https://github.com/zdict/zdict.vim)  
+ 有人因為懶得打指令想要補完，所以弄了個 completion script: [GitHub - zdict/zdict.sh: A collection of shell completion scripts for zdict](https://github.com/zdict/zdict.sh)  
+ 有人因為想用滑鼠選起來就能直接查，所以寫了這個：[GitHub - zdict/zdict.qt: zdict with Qt5 widget](https://github.com/zdict/zdict.qt)  
  
---  
  
## 結論  
  
反正就是很自由啦，連 organizaiton 都是拿 One Taiwan 的圖片產生器來改的：[zdict · GitHub](https://github.com/zdict)，就知道有多北七。XD  
  
我覺得大家應該都要至少要找到一個屬於自己的這種 side project，可以讓你跟一些人 cowork，但又不會有壓力，同時又符合你日常生活的需求。  
  
而且因為彼此想要的功能不一樣，而且又是開放原始碼的專案，所以可以學到自己不會的東西。唯一的小缺憾大概就是，這只是個小確幸的專案，不是什麼大專案，但又何妨？  
  
要練習寫程式的話真的從自身的需求出發就夠了，不需要做一個什麼多偉大多困難的專案，可以等夠熟練的時候再說，希望大家都能找到一個屬於自己的 side project 當作核爆場（誒  
