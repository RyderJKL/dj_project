# requirement

- django
- djangorestframework
- django-filter
- Pillow
- Markdown # Markdown support for the browsable API.
- coreapi
- django-filter  # Filtering support
- django-crispy-forms
- django-guardian

```bash
pip install django djangorestframwork \n
django-filter Markdown Pillow \n
crispy_forms coreapi
```

## install coreapi error
windows 下安装`coreapi`肯能会出现`utf8`的报错，进入方案:
进入`lib/site-packages/pip/compat/__init__.py`,将函数`75`行`console._to_str`中的`utf8`改为`gbk`

!> windows 下安装依赖包经常出错的解决方案
推荐一个网站: [lfd](www.lfd.uci.edu)
