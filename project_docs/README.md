# Definitional documents

`/docs` contains the text documents that describe the decision process, the decision points, the possible decision
values, and the decision trees that should be used to reach prioritization decisions.

We use `mkdocs` to build the documentation website. The `mkdocs.yml` file in the root of the repository contains the
configuration for the website. The `docs` folder contains the markdown files, css, and other assets that are used to 
build the website. 

We are using 'material for mkdocs' to provide the theme and some extensions for the website.

The documents are in markdown for easy editing.

## Local development

To build the documentation locally, you will need to install `mkdocs` and `mkdocs-material`:

```bash
pip install -r requirements.txt
```

Then you can run the development server:

```bash
mkdocs serve
```


## Diátaxis Framework

We are using the [Diátaxis Framework](https://diataxis.fr/) to organize our documentation into four main categories,
oriented around the different ways that people might need to learn about and use SSVC.

Contributors should follow the Diátaxis Framework's [_Map of Needs_](https://diataxis.fr/needs/) to determine where to
put new content. Summarizing the map:

|                      | Tutorials                            | How-to guides                           | Reference                        | Explanation                           |
|----------------------|--------------------------------------|-----------------------------------------|----------------------------------|---------------------------------------|
| what they do         | introduce, educate, lead             | guide, demonstrate                      | state, describe, inform          | explain, clarify, discuss             |
| answers the question | "Can you teach me to...?"            | "How do I...?"                          | "What is...?"                    | "Why...?"                             |
| oriented to          | learning                             | tasks                                   | information                      | understanding                         |
| purpose              | to allow the newcomer to get started | to show how to solve a specific problem | to describe the machinery        | to explain                            |
| form                 | a lesson                             | a series of steps                       | dry description                  | discursive explanation                |
| analogy              | teaching a child how to cook         | a recipe in a cookbook                  | a reference encyclopedia article | an article on culinary social history |


## Documentation Directory Structure

- `/docs/tutorials` - Tutorials
- `/docs/howto` - How-to guides
- `/docs/reference` - Reference
- `/docs/topics` - Explanation
- `/docs/about` - project-level information (e.g., about, contributing, etc.)
- other directories as needed for the website (`/docs/assets`, `/docs/stylesheets`, `/docs/javascript`, etc.)


## Markdown file naming conventions

Previously we had used a more strict naming convention for the markdown files, but we have relaxed that to allow for
more flexibility in organizing content in the future.

## PDF and HTML output

We are no longer generating PDF or single-HTML-all-in-one-file output for the documentation.
This is because the documentation is now organized as a website, and maintaining multiple formats adds a lot of overhead.

We may revisit this decision in the future, but for now we are only generating HTML output in the form of a website.


# Style Guide and How-To

**NOTE:** These conventions were put in place to make a consistent style for the PDF version of the documentation.
Many of them may have been superseded by the move to a website format, but we are keeping them here for now.
We expect that we will need to revisit these conventions as we continue to develop the documentation.

---

In the text, please use the following conventions:
- Names of decision points are capitalized and italics (md is `*` or `_`)
- Values for specific decisions at a decision point are lower case and bold (md is `**` or `__`)
  - Values uppercase at the start of a sentence, but try to avoid such sentence constructions.
- Headings that declare the decision point name or values should not be additionally emphasized. 
  - That is, if the name is the whole heading, don't use emphasis. 
  - If the name is part of another heading, use emphasis. 
- Decision points, decision values, and stakeholder decisions should always be in a link cross-referenced to the table in which they are defined. 

So we would have:
`[_Utility_](#utility)` or `[*Technical Impact*](#technical-impact)` which might have values of `[super effective](#utility)` or `[partial](#technical-impact)`
 
- Names of decisions are italicized (`*` or `_`) and lower case.

For example: the decision is to move forward with `[*scheduled*](#applier-decisions)` priority.

 - [ ] This choice collides with decision point names. However, the cap vs lowercase combined with the anchor crossreference is probably enough for readers to distinguish them. Seek feedback on this.  


- Short summaries after the section header declaring the name of the decision point should be in block quotes. 
  - For example:
```
### Exploitation
> Evidence of Active Exploitation of a Vulnerability
```

  - The short summary should be in title case. 
  - There should not be a blank line between the heading and the block quote


## How To Use Cross References

**NOTE:** These conventions were put in place to make a consistent style for the PDF version of the documentation.
Many of them may have been superseded by the move to a website format, but we are keeping them here for now.
We expect that we will need to revisit these conventions as we continue to develop the documentation.

---

- Cross references to other sections can be accomplished with the `[text](link)` syntax for links.
  - The text to appear goes in `[]`
  - The heading to link to goes in `()`
- Use full heading text, lowercased, with `-` instead of spaces. 
  - for example [Section 2](#current-state-of-practice)
  - See: https://gist.github.com/asabaylus/3071099

### To create an arbitrary anchor
- use HTML, e.g.:
```html
<a name="anchor-name"></a>
```
- see also https://stackoverflow.com/questions/5319754/cross-reference-named-anchor-in-markdown


## Terms quoted from other sources

**NOTE:** These conventions were put in place to make a consistent style for the PDF version of the documentation.
Many of them may have been superseded by the move to a website format, but we are keeping them here for now.
We expect that we will need to revisit these conventions as we continue to develop the documentation.

---

- In order not to collide use of emphasis, italics (`*word*`) should not be used to identify a vocabulary word that is not the name of a decision point.
  - If the word or phrase need not be emphasized, it should simply but put in double quotes (`"`). 
  - If the word or phrase needs to be emphasized because it is critical to understanding the passage and it should stand out from the surrounding text, bold can be used (`**` or `__`).
  - This style should be used sparingly, primarily for the first place that a key term is defined. 

- Comments in the source code use HTML comments:
```
<!-- This is a comment that won't show in the output -->
```

- Obviously don't put sensitive information in the comments.
- Comments should be used to note where editorial decisions have been made to about style. 
- For example, though `*Exposure*` is the decision point, we may still want to talk about exposure generally, and it might be helpful to note in a comment that the word exposure is not emphasized on purpose. 

## Do not use footnotes. 
  
**NOTE:** These conventions were put in place to make a consistent style for the PDF version of the documentation.
Many of them may have been superseded by the move to a website format, but we are keeping them here for now.
We expect that we will need to revisit these conventions as we continue to develop the documentation.

---

- There is a markdown style for footnotes (https://pandoc.org/MANUAL.html#footnote)
  - But right now GFM doesn't support that.
  - Footnotes and asides that were not references in v1 have been written in to the flow of the text. 

- If there is some lengthy aside that is helpful, but is too long to be written into the flow of the text, it should be set off with a `----` (horizontal rule) and marked as an aside and ended with another hrule. 
- This style can only be used for asides that are at least a full paragraph.
- To mark it as an aside, give it a title in block quote format

``` 
----
> aside title

aside content
----
```

- Don't use Headings (`#`, `##`, etc.) because this will interfere with section numbering. 
- It would be good practice to provide an HTML anchor with the same name as the aside title, so we can cross reference the box elsewhere. 


## JSON

- When describing JSON literals in the `.md` documents, they should be marked up as `code literals` using backticks (`). 


## Tables

**NOTE:** These conventions were put in place to make a consistent style for the PDF version of the documentation.
Many of them may have been superseded by the move to a website format, but we are keeping them here for now.
We expect that we will need to revisit these conventions as we continue to develop the documentation.

---

- GFM uses the `pipe_tables` markdown extension by default, so tables should use that format. 
- Tables should avoid HTML or LaTeX literal tables, as those aren't portable.
  - If absolutely necessary, include both. 
- Note that when pandoc renders a pipe table into LaTeX if " the cell contents will wrap, with the relative cell widths determined by the number of dashes in the line separating the table header from the table body. 
  - (For example `---|-` would make the first column 3/4 and the second column 1/4 of the full text width.) " https://pandoc.org/MANUAL.html#tables

- Use the `table_captions` extension
  - In GFM this will render as text, but it will still be helpful.
  - "A caption may optionally be provided with all 4 kinds of tables (as illustrated in the examples below). 
  - A caption is a paragraph beginning with the string `Table:` (or just `:`), which will be stripped off. It may appear either before or after the table."
  - Put `Table:` marker above the table, not below it. 


## Embedding images

**NOTE:** These conventions were put in place to make a consistent style for the PDF version of the documentation.
Many of them may have been superseded by the move to a website format, but we are keeping them here for now.
We expect that we will need to revisit these conventions as we continue to develop the documentation.

---

Use the supported markdown for images where possible and support the link_attributes extension. 
https://pandoc.org/MANUAL.html#images

`![Caption](foo.jpg){width=90%}`

This will render as a figure in latex as long as it is on a line all by itself and the implicit_figures extension to pandoc is used. 
It will render as a normal image in GFM. 

## Spacing

**NOTE:** These conventions were put in place to make a consistent style for the PDF version of the documentation.
Many of them may have been superseded by the move to a website format, but we are keeping them here for now.
We expect that we will need to revisit these conventions as we continue to develop the documentation.

---

- Pandoc Markdown will treat a period (`.`) followed by two spaces (`  `) at the end of a line as a request for a line break. 
- Always use only one space after a period, especially at the end of a line. 

- Use unicode characters for opening and closing double quote marks (`“` and `”`) rather than a straight dumb quote mark (`"`).
- Do not try to use LaTeX conventions of (``) and (''). 

## Notes on References

**NOTE:** These conventions were put in place to make a consistent style for the PDF version of the documentation.
Many of them may have been superseded by the move to a website format, but we are keeping them here for now.
We expect that we will need to revisit these conventions as we continue to develop the documentation.

---

- Would most prefer using `pandoc-citeproc`. 
- GFM does not natively support bibtex citations. However, the pandoc markdown syntax is to use `@referencetag`. 
- Documentation for citation processing:
  - https://pandoc.org/MANUAL.html#citations
- The @ citation syntax shouldn't interfere with @ mentions. GFM only allows @ mentions in issues and pull request.
  - https://guides.github.com/features/mastering-markdown/#GitHub-flavored-markdown

### The preferred citation method is as follows:

**NOTE:** These conventions were put in place to make a consistent style for the PDF version of the documentation.
Many of them may have been superseded by the move to a website format, but we are keeping them here for now.
We expect that we will need to revisit these conventions as we continue to develop the documentation.

---

1. Search [`md_src_files/sources_ssvc.bib`](../doc/md_src_files/sources_ssvc.bib) for the desired reference
2. If it's there, use `[@referencetag]` in the markdown text. For example, the tag in the entry beginning with
```bibtex
    @book{simon1996sciences,
```
is `simon1996sciences`
3. If it's not there, add it to the correct subpart of the bibtex file. (books are together, articles are together, CVSS publications are together, etc.) Use authorYYYYword style for the tags (this is the default Google Scholar naming style, which is a good place to get decently formatted bibtex that you can tidy up). Then use the [@referencetag] in the markdown text. 


Though the `[@tag]` command won't reference on github, the `html` target in the `Makefile` has the right pandoc commands to create a pretty HTML file with a proper references section. 

 



