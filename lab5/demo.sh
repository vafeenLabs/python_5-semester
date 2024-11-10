#!/bin/bash

# curl - утилита работы с запросами 

echo http://localhost:8080/index.html
curl -I http://localhost:8080/index.html

echo http://localhost:8080/picture.jpeg
curl -I http://localhost:8080/picture.jpeg

echo http://localhost:8080/script.js
curl -I http://localhost:8080/script.js

echo http://localhost:8080/styles.css
curl -I http://localhost:8080/styles.css
