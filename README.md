# device_register_table

登記設備借出，並在歸還欄增加帳號限制

## 預先安裝環境
`$python3 -m venv venv`

`$source venv/bin/activate`

`$pip install -r requirenment`
    

## 變更使用IP
    edit config/application.py
    
    APP_URL = env("APP_URL", "http://{youripaddr}:8000/")

## 啟用web server
`$python craft serve --host {youripaddr}`

## 開始使用
browser: http://{youripaddr}:8000

