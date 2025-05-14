$pycodestylePath = "C:\Users\dmitr\Polyedr_project\venv\Scripts\pycodestyle.exe"
Get-ChildItem -Path "C:\Users\dmitr\Polyedr_project" -Filter "*.py" -Recurse |
    Where-Object {$_.FullName -notmatch "venv"} |
    ForEach-Object { & $pycodestylePath $_.FullName }
