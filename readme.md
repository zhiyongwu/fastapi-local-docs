from fastapi import FastAPI

# fastapi swagger 本地化


## 安装依赖
`pip install "fastapi[standard]" fastapi-local-docs `

## 创建 demo.py
```python
import fastapi_local_docs
from fastapi import FastAPI

app = FastAPI(root_path='/api')
fastapi_local_docs.init(app)

@app.get('/')
def health():
    return 'running'
```

## 启动服务

`fastapi dev demo.py`

访问 [http://localhost:8000/docs](http://localhost:8000/docs)