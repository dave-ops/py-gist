# py-gist
converts private github repo into a secret gist repo

## get api key
1. goto https://github.com/settings/apps
2. select personal access tokens > tokens (classic)
3. select:
   [x] gist
   [x] project
4. select expiration (up to you)
5. click generate token
6. copy it

## store the api key as env variable 
```
set /p GITHUB_TOKEN=<key> 
```