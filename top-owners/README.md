# NFT 項目持有數 爬蟲

嘗試過使用送 api request 的方式但無法成功，目前先使用 selenium 來做

## 使用說明
0. 請先安裝 [chrome driver](https://chromedriver.chromium.org/downloads)，並且放到跟 main.py 同目錄
    如果在 windows 檔名是 `./chrome.exe`，請到 DRIVER_NAME 改名 
1. 到 etherscan 的 balances 查看
    - ex: https://etherscan.io/token/0xb183858f744eeff5c86f716b7e93d15a8696fa9a#balances
2. 開啟 chrome 開發工具（F12），找到 `<iframe>` 裡面的 `src` 那段
    - ex: 
        ```
        /token/generic-tokenholders2?m=normal&a=0xb183858f744eeff5c86f716b7e93d15a8696fa9a&s=889&sid=adf6ba12a50546cc51844facdcfc46cf&p=1
        ```
3. 在前頭補上 `https://etherscan.io/`
    變成：`https://etherscan.io/token/generic-tokenholders2?m=normal&a=0xb183858f744eeff5c86f716b7e93d15a8696fa9a&s=889&sid=adf6ba12a50546cc51844facdcfc46cf&p=1`

4. 上面的 url 就可以送出一個 request，並且得到第一頁的結果了
    如果要讓程式找遍所有的結果，需要將上方 url 的最後 &p=1 刪掉
    變成：`https://etherscan.io/token/generic-tokenholders2?m=normal&a=0xb183858f744eeff5c86f716b7e93d15a8696fa9a&s=889&sid=adf6ba12a50546cc51844facdcfc46cf`
    並且將 main.py 裡的 URL 改成上述的值

## 參數說明

1. URL: 參照 `使用說明` 可以獲得 request url
2. LOWER_BOUND: 會抓超過該數量的地址，假如設為 10，那就會抓出超過持有 10 隻的地址出來
3. DRIVER_NAME: 依照自己的 selenium driver 名稱來給