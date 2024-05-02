$rootLocation = Get-Location
$frontFolder = Join-Path -Path $rootLocation -ChildPath "kalosFront"
Start-Process PowerShell -ArgumentList "-Command", "uvicorn main:app --reload"
##$backFolder = Join-Path -Path $rootLocation -ChildPath "SSO"
Start-Process PowerShell -WorkingDirectory $frontFolder -ArgumentList "-Command", "npm run dev"
##Start-Process PowerShell -WorkingDirectory $backfolder -ArgumentList "-Command", "uvicorn main:app --reload"