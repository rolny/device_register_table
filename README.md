# device_register_table
登記設備借出，並在歸還欄增加帳號限制

## 預先安裝環境
`$python3 -m venv venv`

`$source venv/bin/activate`

`$pip install -r requirenment`

`$project install`

## 變更使用IP
    編輯 .env
    APP_URL=http://{youripaddr}:8000

## migration (第一次使用請必先migrate)
`masonite-orm migrate:reset;masonite-orm migrate;masonite-orm seed:run;`

## 啟用web server
`$python craft serve --host {youripaddr}`

## 開始使用
browser：http://{youripaddr}:8000

## 開啟帳號註冊及修改
    編輯 route/web.py
	
    新增註解
	`ROUTES += Auth.routes()`
    
    去掉註解
    #ROUTES += Auth.routes_live()

### 新增帳號
#### 直接輸入網址
    1. browser：http://127.0.0.1:8000/register
#### 從登入頁面轉往register
    1. 從http://127.0.0.1:8000/login
    2. 點擊"Create an Account"
#### 密碼強度
    密碼強度未限制，若要啟用密碼強度，照以下步驟
    1. 編輯app/controllers/auth/RegisterController.py
    2. 去掉註解
    `#"password": "required|strong|confirmed"`
    3. 新增註解
    "password": "required|confirmed",

### 變更密碼
#### 直接輸入網址
    1. browser：http://127.0.0.1:8000/password_reset
#### 從登入頁面轉往register
    1. 從http://127.0.0.1:8000/password_reset
#### 啟用修改
    1. 輸入正確email帳號
    2. 點擊SEND REQUEST
    3. 自動跳轉至change_password頁面
    4. 輸入新密碼
    5. 若變更成功顯示"Password Reset Successfully"

### 移除帳號
#### 請直接修改資料庫
    依照資料庫刪除user資料表的帳號資料

# 不使用帳號變更功能時請關閉帳號註冊及修改

