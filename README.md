서버 실행
```
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

패키지 패킹 하는 방법
```
pip freeze > requirements.txt
```

docker 킬 때 주의 할 점!

local에서 접속하고 싶을 때는 --net host를 빼야지만 접속이 된다.( 외부 접속 용이었던 것이지..)
```
docker run -it -p 8001:8001 cicdtest:0.2 
```

배포 순서 
1. pip freeze > requirements.txt
2. git commit & push