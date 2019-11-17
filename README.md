# 实验室的服务器信息
| 序号 | 品牌 | 显卡                 | 显存       | 内存 | 硬盘        | CPU                                        |
| ---- | ---- | -------------------- | ---------- | ---- | ----------- | ------------------------------------------ |
| 1    | AMAX | GeForce GTX 1080 x 2 | 8119M x 2 | 251G | 447.1G+5.5T | Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz  |
| 2    | DELL | GeForce RTX 2080 Ti  | 11019M     | 62G  | 893.8G+2.2T | Intel(R) Xeon(R) Silver 4210 CPU @ 2.20GHz |
| 3    | DELL | TITAN Xp x 2         | 12196M x 2 | 62G  | 2.2T x 4    | Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz  |


# 环境
```shell
pip install paramiko
```


# 配置文件 config.json
```
{
    "command" : ["nvidia-smi", "ls"],   # 在服务器上执行的命令（确认ip和服务器的对应关系）
    "username" : "",                    # 服务器的登陆账户
    "password" : "",                    # 服务器的登陆密码
    "port" : 22,                        # 服务器的ssh端口
    "process_num" : 100,                 # 进程数量

    "ipv4_mask": "10.201.0.0"           # 服务器所在的网段为 10.201.x.x
}
```


# 运行
```python
python -u search_ip.py
```


# 效率
在 10.201.0.0 网段上进行测试
1. 200个进程，大约6分钟
2. 100个进程，大约11分钟


# 注意
进程数量太大可能导致程序异常终止，而不返回任何结果


