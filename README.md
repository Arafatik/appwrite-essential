# appwrite-essential

> Тестовая среда для изучения appwrite functions

## Использование

Скачать схему appwrite в `.\temp`

```bat
.\scripts\fetch
```

Сделать деплой функции на сервер

```bat
.\scripts\push
```

Создать новую appwrite функцию

```bat
.\scripts\init
```

Установить appwrite cli

```cmd
npm install -g appwrite-cli
Set-ExecutionPolicy RemoteSigned
appwrite client --endpoint https://cloud.appwrite.io/v1
appwrite login
```

## Полезные ссылки

 - [Execute appwrite function from postman](https://github.com/appwrite/appwrite/discussions/4946)
