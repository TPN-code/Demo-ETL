<##
if ($PSScriptRoot) {
    $SPath = $PSScriptRoot
}
elseif ($psISE.CurrentFile){
    $SPath = Split-Path $psISE.CurrentFile.FullPath
}
else{
    $SPath = Get-Location
}
##>

$path = Get-Location
$SPath = Convert-Path $path

Add-Type -Path "$SPath\WebDriver.dll"
$chrome=New-Object OpenQA.Selenium.Chrome.chromedriver

$idPath = $SPath + '\tracking IDs.txt'
$savePath = $SPath + '\full status.txt'

$idPath
$savePath

$test = Test-path $savePath
if ($test -eq $true) {Remove-Item $savePath}

$IDs = Get-Content $idPath


$chrome.Navigate().GoToUrl('https://www.ship24.com/tracking?p=')


foreach($ID in $IDs){

    $chrome.FindElementByXPath('/html/body/app-root/app-quick-signup-modal/div/div/div/button').Click()
    $chrome.FindElementByXPath('/html/body/app-root/app-tracking-result/app-banner/div/div/div[2]/div/div[2]/div/div[2]/app-searchbar/div/div/div/div/div/form/input').SendKeys($ID)
    $chrome.FindElementByXPath('/html/body/app-root/app-tracking-result/app-banner/div/div/div[2]/div/div[2]/div/div[2]/app-searchbar/div/div/div/div/div/form/button').click()

    $status = $null
    while ($null -eq $status) {
        $status = $chrome.FindElementByXPath('/html/body/app-root/app-tracking-result/div[2]/div/div[2]/app-parcel-browser/user-parcel-card[1]/div/div/div[3]/div[2]/app-user-first-event')
        Start-Sleep -Seconds .5
    }

    Write-Host $ID
    Write-Host $status.Text

    $fullStatus = $ID + "`n" + $status.Text + "`n"
    $fullStatus | Out-File $savePath -Append

    $status = $null
}

Invoke-Item $savePath
Write-Host 'ALL DONE!'

$chrome.quit()
exit