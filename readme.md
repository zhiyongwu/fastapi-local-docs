# fastapi swagger 本地化


## 安装依赖
`pip install "fastapi[standard]" fastapi-local-docs `

## 创建 demo.py
```python
from fastapi_local_docs import create_fastapi_app

app = create_fastapi_app(
    root_path='/api',
    version='1.0',
    title='A FastAPI app'
)

@app.get('/')
def health():
    return 'running'
```

## 启动服务

`fastapi dev app.py`

访问 [http://localhost:8000/docs](http://localhost:8000/docs)