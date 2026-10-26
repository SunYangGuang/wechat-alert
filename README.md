# WeChat Alert - 微信群关键词监控

监控指定微信群，出现关键词时弹窗+响铃提醒。

## 环境要求

- Windows 10/11
- 微信 4.1.x（PC版，保持登录状态）
- Python 3.10+（安装时勾选 **Add Python to PATH**）

## 安装步骤

1. 安装 Python（从 python.org 下载，勾选 Add to PATH）
2. 双击运行 `install.bat`，等待依赖安装完成

## 使用方法

1. 确保微信已登录
2. 右键 `start_monitor.bat` → **以管理员身份运行**
3. 看到 `监控运行中...` 就说明成功了
4. 群里出现关键词时会弹窗+响铃3次

## 修改配置

用记事本打开 `wechat_monitor.py`，改顶部两行：

```python
KEYWORD = "下午7点"

TARGET_GROUP_NAMES = [
    "香河东通勤拼车2群",
    "大爱社区业主群1",
    "大爱&绿地拼车群",
]
```

保存后重新启动 `start_monitor.bat`。

## 注意事项

- 监控窗口不要关，关了就停了
- 微信退出重登后需要重新启动监控脚本（会自动重新获取key）
- 首次启动会解密数据库，约10秒，之后秒开
