# py-gist
converts private github repo into a secret gist repo

## get api key
1. goto https://github.com/settings/apps
2. select personal access tokens > fine-grained tokens
4. select expiration
5. click generate token
6. copy it

## store the api key as env variable 
```
set /p GITHUB_TOKEN=<key> 
```

## how to run
```
python src\main.py
```

### demo
sample run
```s
Enter the folder path to flatten: c:\py-gist\src
Enter the output folder path: c:\py-gist\output
Enter Project Name for the Gist: py-gist
Enter your GitHub token: github_pxt_1xxxxxxxxxxxxxxxxzmNm_Axxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Testing GitHub API connection status code: 200
Checking Rate Limit Status: {'resources': {'core': {'limit': 5000, 'used': 0, 'remaining': 5000, 'reset': 1739912283}, 'search': {'limit': 30, 'used': 0, 'remaining': 30, 'reset': 1739908743}, 'graphql': {'limit': 5000, 'used': 0, 'remaining': 5000, 'reset': 1739912283}, 'integration_manifest': {'limit': 5000, 'used': 0, 'remaining': 5000, 'reset': 1739912283}, 'source_import': {'limit': 100, 'used': 0, 'remaining': 100, 'reset': 1739908743}, 'code_scanning_upload': {'limit': 1000, 'used': 0, 'remaining': 1000, 'reset': 1739912283}, 'code_scanning_autofix': {'limit': 10, 'used': 0, 'remaining': 10, 'reset': 1739908743}, 'actions_runner_registration': {'limit': 10000, 'used': 0, 'remaining': 10000, 'reset': 1739912283}, 'scim': {'limit': 15000, 'used': 0, 'remaining': 15000, 'reset': 1739912283}, 'dependency_snapshots': {'limit': 100, 'used': 0, 'remaining': 100, 'reset': 1739908743}, 'audit_log': {'limit': 1750, 'used': 0, 'remaining': 1750, 'reset': 1739912283}, 'audit_log_streaming': {'limit': 15, 'used': 0, 'remaining': 15, 'reset': 1739912283}, 'code_search': {'limit': 10, 'used': 0, 'remaining': 10, 'reset': 1739908743}}, 'rate': {'limit': 5000, 'used': 0, 'remaining': 5000, 'reset': 1739912283}}

Prepared for upload: C:\py-gist\src\api.py as api.py
Prepared for upload: C:\py-gist\src\main.py as main.py
Prepared for upload: C:\py-gist\src\utils.py as utils.py
Attempting to create Gist...
Gist created successfully!

Gist URL: https://gist.github.com/<userid>/<id>
```