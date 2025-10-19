# Prepend a tailored "// Topic: ..." comment to every .cpp/.c file in O:\maggi\c++
# Creates .bak backups and skips files that already contain a Topic comment.

$folder = 'O:\maggi\c++'

# explicit mapping for question files and other known source files
$map = @{
    'question1.cpp'            = 'Basics — input/output and variables'
    'question2.cpp'            = 'Basic operators and expressions'
    'question 3 (statements).cpp' = 'Control flow — statements'
    'question3 (statements).cpp'= 'Control flow — statements'
    'question4_forloops.cpp'   = 'For loop examples'
    'question5.cpp'            = 'Introductory exercise'
    'question6.cpp'            = 'Introductory exercise'
    'question7_fibonachi.cpp'   = 'Fibonacci sequence (recursion/iteration)'
    'question8_whileloop.cpp'  = 'While loop examples'
    'question9_patterns.cpp'   = 'Pattern printing'
    'question10_.cpp'          = 'Basic exercise'
    'question11_.cpp'          = 'Basic exercise'
    'question12_strings.cpp'   = 'String manipulation'
    'question13.cpp'           = 'Exercise — check file for specifics'
    'question14_arrays.cpp'    = 'Array basics'
    'question_15.cpp'          = 'Functions — modular code'
    'question15_fucntions.cpp' = 'Functions — modular code'
    'question16_function.cpp'  = 'Functions and return values'
    'question17_pointer.cpp'   = 'Pointers and pointer arithmetic'
    'question18_strings.cpp'   = 'String utilities and operations'
    'question19_basics.cpp'    = 'Basic concepts / exercises'
    'question20_basic.cpp'     = 'Basic concepts / exercises'
    'question21_array.cpp'     = 'Array operations'
    'question22_banksystem.cpp'= 'Menu-driven bank system (file/console I/O)'
    'question24oops.cpp'       = 'OOPs — classes and objects'
    'question25.c'             = 'C language exercise — check file'
    'question26_arrfn.cpp'     = 'Array functions — linear search (function-based)'
    'question27_arrfn.cpp'     = 'Array functions — utilities'
    'question28_arrfn.cpp'     = 'Array functions — utilities'
    'question29arrfn.cpp'      = 'Array functions — utilities'
    'question30_strfn.cpp'     = 'String functions / helpers'
    'question31_strfn.cpp'     = 'String functions / helpers'
    'question32_arrfn.cpp'     = 'Array functions — utilities'
    'question33_chararr.cpp'   = 'Char array / reverse words in sentence'
    'question34_t2darr.cpp'    = '2D arrays — transpose / matrix ops'
    'question35_2darr.cpp'     = '2D arrays — matrix operations'
    'question36_2darr.cpp'     = '2D arrays — matrix operations'
    'binaryconverter.cpp'      = 'Binary conversion / bit operations'
    'leetcode_3.cpp'           = 'LeetCode problem — longest substring / sliding window'
    'notecounter.cpp'          = 'Counting notes / frequency counter'
    'operators1.cpp'           = 'Operators and precedence'
    'tempCodeRunnerFile.cpp'   = 'Temporary runner / scratch code'
}

Get-ChildItem -Path $folder -Include *.cpp,*.c -File | ForEach-Object {
    $file = $_.FullName
    $name = $_.Name
    $content = Get-Content -Raw -LiteralPath $file

    if ($content -match "(?m)^\s*//\s*Topic:") {
        Write-Host "Skipped $name (Topic already present)"
        return
    }

    # choose topic: explicit mapping first, then heuristics
    if ($map.ContainsKey($name.ToLower())) {
        $topic = $map[$name.ToLower()]
    } else {
        $lc = $name.ToLower()
        switch -wildcard ($lc) {
            '*strings*'  { $topic = 'String manipulation' ; break }
            '*arrfn*'     { $topic = 'Array functions / utilities' ; break }
            '*2darr*'     { $topic = '2D arrays / matrix operations' ; break }
            '*pointer*'   { $topic = 'Pointers' ; break }
            '*fibon*'     { $topic = 'Fibonacci / recursion' ; break }
            '*while*'     { $topic = 'While loop examples' ; break }
            '*for*'       { $topic = 'For loop examples' ; break }
            '*pattern*'   { $topic = 'Pattern printing' ; break }
            '*bank*'      { $topic = 'Bank system / menu-driven' ; break }
            '*leetcode*'  { $topic = 'LeetCode problem' ; break }
            '*binary*'    { $topic = 'Binary conversion / bit ops' ; break }
            '*note*'      { $topic = 'Counting / frequency' ; break }
            Default       { $topic = 'Misc — review file to set precise topic' }
        }
    }

    $comment = "// Topic: $topic`r`n`r`n"
    Copy-Item -LiteralPath $file -Destination ($file + '.bak') -Force
    Set-Content -LiteralPath $file -Value ($comment + $content) -Encoding UTF8
    Write-Host "Prepended topic to $name : $topic"
}