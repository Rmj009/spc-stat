### docker build 
### docker run 

## folder meant:
- `api`

  - 集中所有API, 且分兩部份app與app2 , 兩者共用同個web framework flask, 前者app屬於後端運算, 後者app屬於前端

- `static & templates`

  - flask render html既定格式folder, 與css,img,js 相容

- `swagger`

  - swagger 測試用folder

- `utils`

  - 運算的核心,資料庫連接與查詢供給數據給統計製程指標包含 cpk/ppk等計算 


- `POSTGRESQL_URL_LOCAL_TENANT`

  - 連線 Local **DB** 的 **URL**

- `USER_API_URL`

  - **USER** 使用權限 **API URL**

- `EQUIPMENT_API_URL`

  - **機台** 資訊 **API URL**

- `EQUIPMENT_API_URL_LOCAL`

  - Local **機台** 資訊 **API URL**
  
## 🎻 app.py 參數

- `AppMode`

  - `dev`: 開發使用

    <!---待填  **SSO** 邏輯 方便開發 -->
    
- `Params 根據使用者輸入四項參數收尋資料庫`
  - `'startTime'`
  - `'endTime'`
  - `'workOrderOpHistoryUUID'`
  - `'spcMeasurePointConfigUUID'`

- `跑起來`：

   - `python3 app.py`

## 🎻  API回傳值

- `Capability`
  - `"good"`
  - `"totalNum"`
  - `"goodRate"`
  - `"USL"`
  - `"LSL"`
  - `"UCL"`
  - `"LCL"`
  - `"overallMean"`
  - `"target"`
  - `"range"`
  - `"Cpu"`
  - `"Cpl"`
  - `"Cp"`
  - `"Ck"`
  - `"Cpk"`
  - `"Ppk"`

- `Nelson`
  - `data array`
  - `rule1 array`
  - `rule2 array`
  - `rule3 array`
  -       .
  -       .
  -       .
  - `rule8 array`

## [Change Log](CHANGELOG.md)

