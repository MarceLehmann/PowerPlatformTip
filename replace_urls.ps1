$path = "c:\Users\ML Office\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip\CONTENT\3_OLD"
$files = Get-ChildItem -Path $path -Filter *.html -Recurse

foreach ($file in $files) {
    try {
        $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
        if ($content -match "lehmann.ws") {
            $newContent = $content -replace "lehmann.ws", "lehmannws.wordpress.com"
            Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8
            Write-Host "Updated: $($file.Name)"
        }
    }
    catch {
        Write-Error "Failed to update $($file.Name): $_"
    }
}
