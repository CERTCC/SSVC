# Definitional documents

This folder contains the text documents that describe the decision process, the decision points, the possible decision values, and the decision trees that should be used to reach prioritization decisions.

The documents are in markdown for easy editing. The `version_1` folder is a reformatted version of the paper published at [WEIS 2020](https://weis2020.econinfosec.org/wp-content/uploads/sites/8/2020/06/weis20-final6.pdf). This folder should be considered read-only. Future work should create a `version_2` folder to build on.

The `version*/*.md` files should be limited to one file per section, for easier editing and merging. The current numbering scheme is important so the command line `*` ingests the files in the right order. Three digits (`010`, etc.) are used in case new sections need to be interleaved. A substantive edit to a section should probably be renamed `011`, etc., but we don't have guidance on what counts as "substantive" yet. A total re-write wold be, though.

The file `compile.sh` contains the pandoc command line for creating a single HTML document from the markdown. It also contains the document metadata (title, authors, date) as command-line arguments. This file should be edited to accurately compile the most current document. `compile-v1.sh` should be considered read-only analogous to the v1 folder.

The `*how-to` files contain discussion on document composition and style. Please align any commits with the existing how-to guidance. At present (Aug 2020), the how-to guidance is not yet fixed, but it should only change with community discussion.

The `pdfs` folder contains static documents of prior versions.
