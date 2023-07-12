# Definitional documents

This folder contains the text documents that describe the decision process, the decision points, the possible decision
values, and the decision trees that should be used to reach prioritization decisions.

The current draft should be compiled into `/draft/ssvc.html` for easy viewing, though it may be behind the markdown source
by a couple commits.

The documents are in markdown for easy editing.
All the source files needed to create a polished document are in the [`md_src_files`](md_src_files) folder.
The work on version 1 started with the version of the paper published
at [WEIS 2020](https://weis2020.econinfosec.org/wp-content/uploads/sites/8/2020/06/weis20-final6.pdf).
A copy of this document and other prior drafts is in the `/pdfs` folder.

## Markdown file naming conventions

The `*.md` files should be limited to one file per chapter or section, for easier editing and merging.
The current numbering scheme is important so the command line `*` ingests the files in the right (i.e., ASCII-sort) order.
File names follow the convention `CC_SS_name.md` where:

- `CC` is a zero-padded two-digit chapter number
- `SS` (optional) is a zero-padded two-digit section number
- `name` is a string derived from the first heading in the file

So for example, a file whose content starts with `## Foo` representing the third section of chapter two would likely be named `02_03_foo.md`. 

## Makefile

The [`Makefile`](Makefile) contains pandoc commands line for creating a single HTML and PDF document from the markdown. It also
contains the document metadata (title, authors, date) as command-line arguments. You can:

```bash
$ make all
```
to produce both HTML and PDF output, or do either of
```bash
$ make pdf
$ make html
```
for the respective output.
Output of the `make` commands can be found in `/draft`.

Note that the `Makefile` was used as the basis for the github action
[`.github/workflows/pandoc_html_pdf.yaml`](./github/workflows/pandoc_html_pdf.yaml), which should be maintained in sync 
with the `Makefile` in the future.


The `*how-to` files contain discussion on document composition and style. Please align any commits with the existing
how-to guidance. At present (Aug 2020), the how-to guidance is not yet fixed, but it should only change with community
discussion.

# Thank you

The authors thank the following people for helpful comments on prior drafts: Michel van Eeten as shepherd and the
anonymous WEIS reviewers; attendees at A Conference on Defense (ACoD), Austin TX 2020; Dale Peterson, Ralph Langer, and
attendees at S4, Miami FL 2020; Muhammad Akbar and Manish Gaur (VMWare); David Oxley (McAfee).

