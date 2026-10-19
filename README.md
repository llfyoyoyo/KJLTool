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

## Cloudflare Pages 部署

在 [Cloudflare Dashboard](https://dash.cloudflare.com) → Workers & Pages → 你的项目 → Settings → Builds：

| 配置项 | 推荐值 |
|--------|--------|
| Framework preset | None |
| Build command | （留空） |
| Build output directory | `/` 或留空 |
| Root directory (Optional) | `/` 或留空 |

不要把 Output directory 设成 `viewer`（否则 `jsons/` 不会被发布）。

部署成功后访问：

- `https://你的项目.pages.dev/`（会跳转到 `/viewer/`）
- 或直接打开 `https://你的项目.pages.dev/viewer/`

若页面完全打不开：检查部署是否绿色成功；国内网络偶发无法解析 `*.pages.dev`，可绑定自定义域名，或换网络/代理再试。
