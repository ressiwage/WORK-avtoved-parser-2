# получение access токена

1. получить id приложения ответственного за токен (в данном случае 7394227)
2. выполнить запрос, скопировать код из адресной строки https://oauth.vk.com/authorize?client_id=ИД_ПРИЛОЖЕНИЯ&display=page
&redirect_uri=https://api.vk.com/blank.html&scope=photos,wall,groups,offline
&response_type=code 
3. зайти на страницу https://vk.com/editapp?id=ИД_ПРИЛОЖЕНИЯ и в разделе настройки скопировать защищенный ключ
4. выполнить запрос https://oauth.vk.com/access_token?client_id=ИД_ПРИЛОЖЕНИЯ
    &client_secret=ЗАЩИЩЕННЫЙ КЛЮЧ&redirect_uri=https://api.vk.com/blank.html
    &code=КОД ИЗ П.2
5. скопировать токен, он вернется в формате json
