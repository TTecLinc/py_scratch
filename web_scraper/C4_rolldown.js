{"_id":"roll_zhihu","startUrl":["https://www.zhihu.com/topic/19559424/top-answers"],"selectors":[{"id":"cont","type":"SelectorElementScroll","parentSelectors":["_root"],"selector":"div.List-item:nth-of-type(-n+66) ","multiple":true,"delay":"500"},{"id":"title","type":"SelectorText","parentSelectors":["cont"],"selector":"h2","multiple":false,"regex":"","delay":0},{"id":"name","type":"SelectorText","parentSelectors":["cont"],"selector":".AuthorInfo-name div.Popover","multiple":false,"regex":"","delay":0},{"id":"tale","type":"SelectorText","parentSelectors":["cont"],"selector":"button.ContentItem-action:nth-of-type(1)","multiple":false,"regex":"","delay":0}]}
