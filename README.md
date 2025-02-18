# py-gist

1. Converts a **private GitHub repository** into a **secret Gist repository** with url.
2. **Supply it with the path** to the source files, and your private GitHub personal access token.
3. **It will flatten out the folder structure** into single files within an output folder.
```
   src/
   ├── module1/
   │   ├── sub_module1/
   │   │   └── file1.py
   │   └── file2.py
   └── module2/
   └── file3.py
```
4. **output**
```
   output/
   ├── module1_sub_module1_file1.py
   ├── module1_file2.py
   └── module2_file3.py
```
5. **Upload them to Gist** for secure sharing.
6. **Return a public URL** that you can share without needing to grant access to your private GitHub repository or making it public.

## Project Structure
```
py-gist/
├── src/
│   ├── __init__.py
│   ├── api.py
│   ├── main.py
│   └── utils.py
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── start.bat
└── start.sh
```

## Obtaining a GitHub API Key
1. Navigate to [GitHub Developer Settings](https://github.com/settings/apps).
2. Under "Personal access tokens", select **Fine-grained tokens**.
3. Choose an expiration date for your token.
4. Click **Generate token**.
5. **Copy** the generated token securely.

## Storing the API Key as an Environment Variable
To set the GitHub token as an environment variable in Windows Command Prompt, use:
```cmd
set /p GITHUB_TOKEN=<key>
```
For other operating systems, follow the respective method to set environment variables.

## Running the Script
Execute the script with the following command:
```
python src/main.py
```

## Demonstration
Sample Run:
```sh
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
```
[https://gist.github.com/dave-ops/1199901fea1e561a5880c4cec06d1bca](https://gist.github.com/dave-ops/1199901fea1e561a5880c4cec06d1bca)

### Virtual Environment

if you need to run in a virtuaL environment
```cmd
python -m venv venv --prompt gist
venv\Scripts\activate
pip install -r requirements.txt
```

```bash
python -m venv venv --prompt gist
source venv/bin/activate
pip install -r requirements.txt
```

## Github

### pr requires linear history
```
git rebase main
git push --force-with-lease origin your-branch-name
```