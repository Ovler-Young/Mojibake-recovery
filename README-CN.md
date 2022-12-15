# 乱码恢复

这是一个乱码恢复工具，可以帮助你恢复乱码。

它尝试使用 GBK，utf-8，BIG5，euc_kr 等编码进行重新编码和解码，以帮助你恢复乱码。

## 使用

这是一个命令行工具，你可以像这样使用它：

```bash
$ python main.py 
    输入待处理文本: {your text}
```

## 例子

```bash
python main.py 
```

![image-20221215152356085](./assets/image-20221215152356085.png)

## 灵感

这是我为了一个线上跑团做的工具。在那个游戏中，DM 会隐藏一些信息，然后使用一种编码对信息进行编码，使用另一种编码对信息进行解码，这样玩家猜不到藏了啥。所以我做了这个工具来解码。

顺便安利这个团，在[这里](https://www.nmbxd1.com/t/52010487)可以找到。DM 很忙，目前是鸽子。

由 [乱码恢复](http://www.mytju.com/classcode/tools/messyCodeRecover.asp) 启发，基于 [MojibakeRecover](https://github.com/Dreace/MojibakeRecover) 二次开发。
