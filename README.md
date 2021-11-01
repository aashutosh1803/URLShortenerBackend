# URLShortenerBackend

This repository is backend repo for URL shortener.Frontend code repo can be found at https://github.com/aashutosh1803/urlShortner

This repo contains two AWS lambda functions - 

1. create-short-url -  This lambda function hosts as POST request which takes long url as parameter and returns short token based on alphanumeric algorithm and conditional expression of dynamo db

2. get-long-url - This lambda function works as GET request which takes short url token as parameter and returns long url associated with it
