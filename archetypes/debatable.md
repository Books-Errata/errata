{{- $p := "" -}}
{{- with findRESubmatch `^p(\d+)` .File.ContentBaseName 1 -}}{{- $p = index (index . 0) 1 -}}{{- end -}}
---
# 出入族条目，程度为「可商榷」：现译可以成立，只是另有值得考虑的译法，或现有证据不足以断定现译有误。
# 正文用「讨论」而不是「问题」。错误、不够精确用 --kind entry，改写与删节用 --kind comparison。
#
# 标题规则：条目标题一律以原文为准，不用现译、也不用建议译法作标题。按以下优先次序：
# 1. 词语或短语层面：用原文词语，按原语言规范大小写，如 periodically
# 2. 整句：用症结（结构、搭配、否定范围、指代等）作标题
# 3. 找不出单一症结：用原句开头几个词加省略号
# 4. 原句开头不足以辨认：用简短中性的中文描述，说明位置和内容，不带判断
title: ""
# 标题语言一般自动判断：不含汉字的标题按原书语言处理。判断有误时取消下一行注释并填写，如 ja
# title_lang: ""
# 收录日期，新建时自动填入，用于首页「最近收录」
date: {{ .Date | time.Format "2006-01-02" }}
# 位置。三项都是可选的，有哪项写哪项：
#   page_cn    中译本页码。文件名以 p+页码 开头时（如 p123-xxx.md）自动填入，同时填入 weight 用于排序
#   page_orig  原书页码
#   location   没有页码时（如看电子书）写章节等位置，如「第七章」「第三章第二节」「后记」
# 没有页码的条目排在有页码的条目之后。想按章节排序，可以手动给 weight 填数字，如第七章填 700
{{ with $p }}weight: {{ . }}{{ else }}weight: 0{{ end }}
page_cn: "{{ $p }}"
page_orig: ""
location: ""
# 现译、建议译法的简短形式；长句条目留空
current: ""
suggested: ""
# 类型，只选一个：names 译名／word-sense 词义／syntax 句法／rhetoric 修辞与语气／omission 漏译／addition 增译
# 各类的说明和判断顺序见 archetypes/entry.md 或站内「类型」页
types: []
degree: 可商榷
# 涉及的跨书术语，填英文 slug，如 [totalitarianism]；可选
terms: []
# 「未修订」或「已修订」；已修订时在 revised_in 注明哪一印
status: 未修订
revised_in: ""
# false 表示「待核实」；有他人对照原书核实后改为 true
verified: false
---

## 原文

> 〔原文引文，以说明所需为限，一般不超过一两句〕

## 现译

> 〔现译引文，照录原文〕

## 讨论

〔说明为何另有考虑。只针对文本，不下定论；如果只是个人偏好，如实说明。〕

## 建议

〔可供比较的译法。〕

## 依据

〔可核对的依据。〕
