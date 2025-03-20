# Code

This directory holds helper scripts that can make managing or using SSVC easier.

## csv-to-latex

This python script takes a CSV of the format in the `../data` directory and gets you (most of the way) to a pretty decision tree visualization. It creates a LaTeX file that can create a PDF (and from there, a PNG or whatever you want).

`python SSVC_csv-to-latex.py --help` works and should explain all your options.
When the script finishes, it will also print a message with instructions for creating the PDF or PNG from the tex. A potential future improvement is to call `latexmk` directly from the python script.

Example usage:

```
 python SSVC_csv-to-latex.py --input=../data/ssvc_2_deployer_simplified.csv --output=tmp.tex --delim="," --columns="0,2,1" --label="3" --header-row --priorities="defer, scheduled, out-of-cycle, immediate"
```

Dependencies: LaTeX.
To install latex, see <https://www.latex-project.org/get/>
`latexmk` is a helper script that is not included in all distributions by default; if you need it, see <https://ctan.org/pkg/latexmk/?lang=en>
