# Notes on References

- Would most prefer using pandoc-citeproc. 
- GFM does not natively support bibtex citations. However, the pandoc markdown syntax is to use @referencetag. 
- Documentation for citation processing:
  - https://pandoc.org/MANUAL.html#citations
- The @ citation syntax shouldn't interfere with @ mentions. GFM only allows @ mentions in issues and pull request.
  - https://guides.github.com/features/mastering-markdown/#GitHub-flavored-markdown

## The preferred citation method is as follows:

1. Search [`md_src_files/sources_ssvc.bib`](md_src_files/sources_ssvc.bib) for the desired reference
2. If it's there, use `[@referencetag]` in the markdown text. For example, the tag in the entry beginning with
```bibtex
    @book{simon1996sciences,
```
is `simon1996sciences`
3. If it's not there, add it to the correct subpart of the bibtex file. (books are together, articles are together, CVSS publications are together, etc.) Use authorYYYYword style for the tags (this is the default Google Scholar naming style, which is a good place to get decently formatted bibtex that you can tidy up). Then use the [@referencetag] in the markdown text. 


Though the `[@tag]` command won't reference on github, the `html` target in the `Makefile` has the right pandoc commands to create a pretty HTML file with a proper references section. 

## Do not use footnotes. 
- There is a markdown style for footnotes (https://pandoc.org/MANUAL.html#footnote)
  - But right now GFM doesn't support that. 
- Footnotes and asides that were not references in v1 have been written in to the flow of the text.

 



