如果佈署container在default的network
docker會自動創建三種不同的ethernet interface並連接
連接至docker0 bridge


開啟的docker container檢查方法
```
docker exec [container name] sh
ip add
ip route

or

docker inspect [container name] bridge

```


NAT masquerate