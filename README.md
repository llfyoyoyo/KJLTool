# KJLTool — 酷家乐方案场景查看器

基于 Three.js 的酷家乐（Kujiale）方案 JSON 本地/在线查看工具：树形结构、3D 预览、孔位/布尔开槽、搜索与节点属性面板。

## 本地运行

需要 Python 3。

```bat
start.bat
```

或：

```bash
python serve.py --host 127.0.0.1 --port 8080
```

然后打开 http://127.0.0.1:8080/viewer/

也可在页面中选择 / 拖拽 JSON 文件加载。

## 目录

- `viewer/` — 前端页面与 Three.js 资源
- `jsons/` — 示例方案（体积较大的样例未纳入仓库）
- `serve.py` — 静态文件服务（修正 Windows 下 `.js` MIME）

## 说明

仓库默认只保留少量较小示例 JSON。完整方案请自行放入 `jsons/` 或通过页面上传。
