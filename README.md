# 推敲·译著勘误

https://errata.hone.ink

这不是出版社的官方勘误，只是普通读者对照原文阅读中译本时的发现与记录；因为事关公共利益，所以公开分享出来。

收录误译、漏译、专名与术语误识，以及删节与改写的对照，按书和类型整理。

## 参与

不会用 Git 也可以参与：

- **有 GitHub 账号**：在本仓库的 [Issues](https://github.com/Books-Errata/errata/issues/new/choose) 中选「提交新勘误」或「指正已有条目」，按表单填写。
- **没有 GitHub 账号**：发邮件到 errata@hone.ink，格式见站上的[参与贡献](https://errata.hone.ink/contribute/#email)页。
- **熟悉 Git**：直接提交 pull request，文件的写法见 [CONTRIBUTING.md](CONTRIBUTING.md)。

提交之前，请先读一遍[收录原则与写作要求](https://errata.hone.ink/contribute/#principles)。

## 本地预览

需要 [Hugo](https://gohugo.io/)，版本见 `hugo.toml` 中的 `[module.hugoVersion]`；部署和检查流程都从那里读取版本号。

```bash
hugo server --cleanDestinationDir
```

然后打开 http://localhost:1313 。搜索功能要先生成索引，需要 Node.js：

```bash
hugo build && npx pagefind@1.5.2 --site public --serve
```

然后打开 http://localhost:1414/search/ 。

## 许可

本仓库的内容以 [CC BY-SA 4.0](LICENSE) 授权。条目中引用的原文与译文，仅用于评论和学术讨论，著作权仍归原权利人所有，不在上述许可范围之内。详见站上的[关于](https://errata.hone.ink/about/#license)页。
