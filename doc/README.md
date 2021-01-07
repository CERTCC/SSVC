# Definitional documents

This folder contains the text documents that describe the decision process, the decision points, the possible decision values, and the decision trees that should be used to reach prioritization decisions.

The current draft should be compiled into `ssvc_v#.html` for easy viewing, though it may be behind the markdown source by a couple commits.

The documents are in markdown for easy editing. 
All the source files needed to create a polished document are in the `md_src_files` folder.
The work on version 1 started with the version of the paper published at [WEIS 2020](https://weis2020.econinfosec.org/wp-content/uploads/sites/8/2020/06/weis20-final6.pdf). 
A copy of this document and other prior drafts is in the `pdfs` folder. 


The `*.md` files should be limited to one file per section, for easier editing and merging. The current numbering scheme is important so the command line `*` ingests the files in the right order. Three digits (`010`, etc.) are used in case new sections need to be interleaved. A substantive edit to a section should probably be renamed `011`, etc., but we don't have guidance on what counts as "substantive" yet. A total re-write wold be, though.

The `compile*.sh` files contain pandoc command line for creating a single HTML document from the markdown. It also contains the document metadata (title, authors, date) as command-line arguments. 

The `*how-to` files contain discussion on document composition and style. Please align any commits with the existing how-to guidance. At present (Aug 2020), the how-to guidance is not yet fixed, but it should only change with community discussion.


# Thank you
The authors thank the following people for helpful comments on prior drafts: Michel van Eeten as shepherd and the anonymous WEIS reviewers; attendees at A Conference on Defense (ACoD), Austin TX 2020; Dale Peterson, Ralph Langer, and attendees at S4, Miami FL 2020; Muhammad Akbar and Manish Gaur (VMWare); David Oxley (McAfee).

