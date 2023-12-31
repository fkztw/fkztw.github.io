Title: TSCC 2015 Notes and Thoughts  
Slug: tscc-2015-notes-and-thoughts  
Date: 2015-09-15 00:18:11  
Authors: fkz  
Category: Contest  
Tags: Thought, TSCC, HPC, Competition, Cluster  
Summary: Notes and Thoughts about the Taiwan Student Cluster Competition 2015  
  
  
又是一篇遲來的文章  
這比賽是在今年的 6/4, 6/5 兩天比的  
心得跟紀錄拖到現在才寫...  
  
---  
  
TSCC 2015 (第五屆全國學生叢集電腦競賽)  
第一次參加，也是最後一次，  
太晚知道這個比賽了，有點可惜。  
這個比賽真的蠻封閉的，  
而且又限定只有高中生和大學生可以參加，  
研究所以上只能當領隊給予指導，不得參賽。  
然後基本上冠軍都是清大在拿，  
因為他們有專門的實驗室在從事這方面的研究，  
然後也很積極的去栽培大學部的學生投入這個比賽，  
有很多學長姊及實驗室的資源可以使用。  
不然光是主機需要的配備以及 Infiniband 的專門網卡就要花掉幾萬元，  
對學生來說不算小的開支，  
但對實驗室來說不過是筆小小的經費罷了。  
而且他們的實驗室也有好幾篇論文是在做這方面的研究，  
總之，  
清大投入的心力以及資源都是其他學校及不上的。  
  
特殊的是，  
我們這組是唯一的跨校聯隊，  
其他組的人全部都是同校的，  
真的覺得高中時參加的社團很神奇，  
緣分很妙，能認識你們很榮幸。  
雖然跨校的缺點就是很難挪出大家的共同時間一起練習，  
但用線上討論跟遠端的環境克服倒也沒那麼困難就是。  
明年應該也還會繼續維持跨校聯隊吧?  
只可惜我已經畢業不能參加啦  
  
其實整個比賽下來，感覺沒幫上什麼忙，只有各種打雜：  
扛東西、插拔線、重開機、Debug、通靈CUDA(失敗)  
第一天一大早，  
一手各帶一組螢幕鍵盤滑鼠，跟 dv 共帶了三組到現場。  
（這比賽一組六人，有 4 台 server 得操作，  
但現場只提供一組螢幕鍵盤，也沒提供 KVM。  
真不知道明年不是辦在新竹的話要怎麼帶這麼多鍵盤螢幕）  
  
第一天早上會給時間進行環境安裝測試，  
參賽者可測試自己的環境建置有沒有問題，  
不過我們在賽前其實只有把繁瑣的操作步驟打在 Hackpad 上，  
並沒有寫成 Script  
所以在測試的時候我們是其他四人一人一台，  
憑手速照著 Hackpad 上的流程建環境，  
但這畢竟不是辦法，  
所以我跟喜德便利用時間把伊達的安裝指南寫成一份 shell script，  
上午的環境測試完之後，  
四顆硬碟會被主辦單位收回，換成全新的硬碟。  
  
下午比賽正式開始，  
用早上臨場寫的 script 開始安裝 4 台 server ，  
檢查了一下，  
發現 Infiniband 的部份有問題，所以又花時間檢查了一下，  
(結果後來發現好像是我們自己搞錯燈號...)  
然後又遇到其中一台的硬碟有問題，  
要求主辦單位更換另外一顆硬碟，  
就這樣大約過了一個半小時左右  
(其實花了比預期多蠻多時間的，讓我們有點緊張)  
之後確定沒啥問題後，就開始燒機，  
把 4 台共 32 核、96 GB RAM 的 servers 操到資源用光跑 HPL，  
因為資源耗光了，也不太能在伺服器上做其他事，  
所以就個人準備自己負責的部份，然後還有享用下午茶點，  
約莫一個半小時跑出 345 Gflops，  
(中間有台主機跑到一半畫面黑掉，一度以為跑到當機，  
結果還好只是螢幕線接觸不良，虛驚一場，畢竟要重來的話時間根本不夠。)  
後來我們自己算了一下 Gflops，大概是理論值的 92%，據說還算不錯。  
(後來在評審時段也被證實是所有參賽八組裏面 HPL 部份最出色的)  
  
第一天剩下的時間就拿來跑 Einstein Toolkit，  
不過狀況似乎也不是很順利，  
沒能在第一天結束時間前解決，遇到點小問題，得留到第二天。  
其實這時進度有點落後了，  
還有 LAMMPS 跟第二天才會公佈的 CUDA 題沒解決。  
  
之後跑去參觀了一下新蓋好的原子輻射中心招待所，  
主辦單位國網中心安排讓學校不在新竹的學生住宿在此，  
還蠻漂亮的，雖然一進入就聞到有點刺鼻的裝潢味。  
但因為唸交大，還是得乖乖回去住學校宿舍。  
  
接下來就回社辦利用時間跟 dv 準備 CUDA 相關的東西，  
希望能在第二天見到題目之前，  
再多多惡補些 CUDA 跟平行運算相關的知識。  
大概到半夜3點多才睡吧。  
(其中意外發現PTT上有一個還不錯的 CUDA 入門系列，  
整理在這 [Nice Series of CUDA Tutorials on ptt.cc | Just for noting](https://fkz.github.io/posts/2015/08/15/nice-series-of-cuda-tutorials-on-ptt-cc/))  
  
隔天一早9點，又到國網中心繼續第二天的比賽，  
小趴和喜德繼續處理昨天的 Einstein Toolkit 問題，  
divazone 則是準備他負責的 LAMMPS 部份，  
我跟 dv 還有伊達則是在 CUDA 題目公佈後就開始著手研究 CUDA 的部份。  
最後 Einstein Toolkit 跟 LAMMPS 的部份我記得是都有跑出來，  
但結果好像普通。  
但 CUDA 的部份我們把想法和改好的程式碼下去跑，  
就是跑不出預期的結果，所以沒有成功。  
(果然只靠前一天惡補是不靠譜的啊)  
  
比賽到中午結束，  
吃完午餐後便開始一組一組的評審面試問答。  
輪到我們這組的時候，  
果不其然，評審都對我們為什麼採用 [Scientific Linux 7](https://www.scientificlinux.org/) 很好奇  
因為其他組都使用一個月前賽前解說提供的環境 Cent OS 6 or 7  
  
> Scientific Linux 是從 Red Hat Enterprise Linux 衍生的 distro，  
> 由歐洲核子研究組織(CERN) 中的費米實驗室(Fermilab) 主持，  
> 提供一個專門用於科學運算的 Linux Distro，  
> 更多相關資訊可以參考  
> [About | Scientific Linux](https://www.scientificlinux.org/about/)  
  
我們便把這個主要原因向評審們說明，  
以及一些採用 Intel 的商用 compiler icc 而不是使用 gcc 等等的一些細節。  
然後還有其他幾題的思路以及為什麼沒有跑出結果的原因。  
評審時間大概歷時 10 ~ 15 分鐘左右就結束了。  
所有組都報告完後，  
所有參賽者跟領隊還有國網中心的工作人員都集中到一間視聽教室，  
然後開始一個算是頒獎前的所有人的討論時間，  
評審先就所有題目的解法大略講過一遍，  
(發現我們對於 CUDA 題原先的想法跟評審公佈的相同，  
但我們考慮的太多，把題目想的太難，  
一方面也是跟 CUDA 不夠熟，所以沒寫出來)  
然後有任何問題或建議都可以提出來，  
提問的狀況蠻熱烈的就是，  
我偷偷提了個冷氣環境的要求，  
在國網中心的大廳忍受一堆 CPU 燒到 100% 和 GPU 的廢熱實在是很熱呀，  
相較於在系計中碰機器的時候都是在十幾度的冷氣環境下，  
身為一個怕熱的肥宅實在有點無法忍受就是。  
  
熱烈的討論時間之後就是頒獎時間。  
頒獎的人我也記不太得，  
最後我們拿到佳作，  
雖然沒有拿到我們賽前希望的前三名，  
但畢竟初出茅廬，這樣的成績也還算不錯啦。  
真的感謝隊友們。  
  
其實比賽結束完後，  
在竹科裡的托斯卡尼尼餐廳有個慶功宴，  
但我因為當 SA 的助教，  
剛好那天晚上得講課，  
只好放棄吃慶功宴，  
比賽結束後，把設備拿回社辦，  
稍微備課一下後，晚餐也沒吃就跑去上課了  
但因為沒吃過托斯卡尼尼的餐點，  
所以請 dv 幫我外帶回交大，  
上完課後9點多才吃XD  
  
最後附上一張四校聯隊的參賽證跟獎牌  
![TSCC 2015 badge & medal](/files/thought-about-tscc-2015/TSCC2015.jpg)  
希望明年可以有更好的成績呢  
  
噢 對了 還得感謝小飛機的指導  
沒有他的話，我大概也不會知道這個比賽。  
附上他當年參賽的心得文 [TSCC 個人心得](http://blog.night9.cc/tscc/)  
還得感謝交大資工系計中  
借了兩張 Infiniband 網卡跟網路線  
不然我們應該沒辦法在事前碰到 Infiniband  
  
---  
  
以下是這次官方發佈的參賽內容:  
  
<http://event.nchc.org.tw/2015/tscc/>  
  
TSCC (Taiwan Student Cluster Competition) 由台灣國家高速網路中心（簡稱國網中心）舉辦的台灣全國學生叢集電腦競賽，限高中生與大學生參加（研究生不可參加，但可擔任教練）。  
  
以前都只有耳聞這個比賽，但沒參加，大學最後一年，因為一些緣分，和高中社團認識的一些人組成了一支橫跨中央、交大、中教大、竹教大的四校聯隊，不知道是不是這比賽第一支聯隊，因為這比賽通常是以校為單位組隊，主要原因是因為高效運算需要的設備成本對學生來說並不便宜，以校為單位的隊伍比較容易向學校申請一些相關經費，為校爭光等等之類的。而清大在這比賽一直是衛冕者，主要是因為他們在這方面真的投入蠻多心力的。  
  
因為以前沒碰過高效運算、平行運算或是叢集運算這方面的東西，想說藉著比賽讓自己學習也未嘗不是件好事，但沒碰過就比較辛苦一點，一堆專有名詞都不太懂，只好寫下來紀錄一下。  
  
2015 的決賽內容:  
  
### LAMMPS  
  
LAMMPS主要是由美國能源部Sandia National Laboratories所開發之GNU開放軟體(open source)，它是一個以古典分子動力學為主的模擬應用程式，並附有蒙地卡羅、耗散粒子動力學等模擬方法，可模擬包含液態、氣態、固態、膠質等不同物質之結構、動力學、力學、…等微觀材料物性質之軟體，尺度可模擬數百至數十億顆原子。LAMMPS更支援個人電腦、大型平行運算主機、或GPU顯卡等設施執行運算，編譯之程式為C + +，並支持MPI、OpenMP與CUDA程式。並且是一個被設計成易於修改或擴展新的原始碼，因此可讓使用者免費使用或修改。  
  
LAMMPS網址為: <http://lammps.sandia.gov/>  
  
---  
  
### Einstein toolkit  
  
Einstein toolkit為一求解初值邊界問題的開源科學模擬程式。主要應用在強重力場下的極端天文物理研究，如黑洞的形成及演化、中子星與黑洞碰撞、重力波計算等其他廣義的相對論磁流體系統，以提供未來重力波相關天文觀測所需要的理論模型。Einstein toolkit 基於Cactus 的插件式設計，支援MPI、OpenMP 以及向量擴展指令集，提供一般模擬過程所需要的元件，如高階有限差分、顯式時間演化積分、結構化自適應網格(structured adaptive mesh refinement)等，而研究者可著重在科學插件的撰寫與組合，控制模擬流程，充分發揮高速計算主機效能。目前主要的開發者為美國、德國、與加拿大的數值相對論研究群。  
  
+ [Einstein toolkit](http://einsteintoolkit.org/)  
+ [Cactus Framework](http://cactuscode.org/)  
  
---  
  
### 多核心高效能程式調教  
  
隨著多核心系統日益普遍，無論桌上型電腦、筆記型電腦甚至平板電腦或智慧型手機皆採用多核心處理器。如何充分使用多核心處理器所帶來的效能優勢進行工程科學計算，成為研究人員重要的課題。  
  
多核心高效能程式調教試題將以工程科學計算作為案例提供Serial程式，參賽隊伍將可依計算環境、演算法特性等，透過平行程式語言(如：OpenMP、MPI、CUDA、OpenCL等)在競賽中所架設之環境進行平行效能測試。  
  
希望參賽者利用對題目的了解、分析平行效率的瓶頸與瞭解平行程式撰寫，調整平行計算環境的設定，進而發揮最佳的平行計算效能；藉此增加對高速計算軟硬體環境之經驗。  
