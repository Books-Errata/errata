{{- $p := "0" -}}
{{- with findRESubmatch `^p(\d+)` .File.ContentBaseName 1 -}}{{- $p = index (index . 0) 1 -}}{{- end -}}
---
# 标题规则：条目标题一律以原文为准，不用误译、也不用建议译法作标题。按以下优先次序：
# 1. 词语或短语层面的问题：用原文词语，按原语言规范大小写，如 les Trente Glorieuses
# 2. 整句译错：先找症结（导致误解的那个结构、搭配、否定范围、指代等），用症结作标题，如 the last man to …
# 3. 找不出单一症结：用原句开头几个词加省略号
# 4. 原句开头不足以辨认，或是漏译、删节等成段问题：用简短中性的中文描述，说明位置和内容，
#    如「第五章论战后福利制度的一段」，不带判断
title: ""
# 中译本页码，用于排序。文件名以 p+页码 开头时（如 p123-trente-glorieuses.md）自动填入
weight: {{ $p }}
page_cn: "{{ $p }}"
page_orig: ""
# 删节与改写对照一般不填 current 和 suggested
current: ""
suggested: ""
# 类型：删节与改写对照。只做对照，不定性；不与其他类型并用
types: [abridgment]
# 涉及的术语，填 content/terms/ 下的英文 slug，如 [totalitarianism]；可选
terms: []
# 「未修订」或「已修订」；已修订时在 revised_in 注明哪一印，如「2023年5月第4次印刷」
status: 未修订
revised_in: ""
# false 表示「待核实」；有他人对照原书核实后改为 true
verified: false
---

## 原文

> 〔原文引文或内容概述；成段内容可概述，只引说明位置所需的一两句〕

## 现译

> 〔对应位置的现译；如译本此处无对应文字，写明「译本此处无对应文字」〕

## 对照说明

〔并列说明两者的差异：删去了什么、合并或改写成了什么。不使用「问题」「错误」等词，不判断性质，不推测原因。〕
