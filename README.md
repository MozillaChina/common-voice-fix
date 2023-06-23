# commonvoice-fix

## src 介绍

### tagger

未来打算开人工标注的时候（粗略的筛选过）

frontend写一个简陋的前端，过/不过/待定几个按钮，一个文本框，就够了。
backend提供一个api请求句子（id管理）的get，和接收结果的post，负责维护数据库，也够了。（需要VPS）
甚至如果直接允许前端访问数据库暴露出来，一个云数据库也足够了。

（或者不设VPS，用fastapi写一个serverless服务也可以）

### analyse

粗筛过程中对语料的筛选和分析

