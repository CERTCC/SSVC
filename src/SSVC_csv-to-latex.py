#!/usr/bin/python

#  Copyright (c) 2025 Carnegie Mellon University and Contributors.
#  - see Contributors.md for a full list of Contributors
#  - see ContributionInstructions.md for information on how you can Contribute to this project
#  Stakeholder Specific Vulnerability Categorization (SSVC) is
#  licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
#  with this Software or contact permission@sei.cmu.edu for full terms.
#  Created, in part, with funding and support from the United States Government
#  (see Acknowledgments file). This program may include and/or can make use of
#  certain third party source code, object code, documentation and other files
#  (“Third Party Software”). See LICENSE.md for more details.
#  Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
#  U.S. Patent and Trademark Office by Carnegie Mellon University

##########
## put import statements here
import optparse, sys, string, glob, re
from optparse import OptionParser

##############################################################################


def initialize_options():
    parser = optparse.OptionParser(
        description="""Take a CSV file as input
	 that describes a decision tree exhaustively, and produce a LaTeX
         file that will make a pretty version of the tree."""
    )
    parser.add_option(
        "-i",
        "--input",
        dest="filelist",
        type="string",
        default="stdin",
        help="input file(s). may be a glob, but will run all \
    output together. Defaults to standard input.",
    )
    parser.add_option(
        "-o",
        "--output",
        dest="out_file",
        type="string",
        default="stdout",
        help="Defaults to stdout.",
    )
    parser.add_option(
        "-d",
        "--delim",
        default="	",
        help="identifies delimiter\
    for the input data (--input). May be any number of characters. Tab default",
    )
    ##########
    ## put other option definitions here
    parser.add_option(
        "-l",
        "--label",
        default="5",
        type="int",
        help="identifies column in input file that contains the label for the leaf\
      node. For SSVC, this label is the decision. These are python list ranges,\
      so first column is 0.",
    )
    parser.add_option(
        "-c",
        "--columns",
        default="1,2,3,4",
        type="string",
        help="identifies columns in input file to use, and the order to use them.\
      Should be in the form of a comma-separated list, such as 2,4,3.\
      Python list ranges start at 0.",
    )
    parser.add_option(
        "--header-row",
        action="store_true",
        dest="headerRow",
        help="Boolean indicating whether the input file has a header row with names\
    for the columns. Default is to expect a header row. \
    To use --names, --no-header-row must be set",
    )
    parser.add_option(
        "-H",
        "--no-header-row",
        action="store_false",
        dest="headerRow",
        help="Boolean indicating whether the input file has a header row with names\
    for the columns. To use --names, --no-header-row must be set",
    )
    parser.add_option(
        "-n",
        "--names",
        type="string",
        default="Exploitation,Virulence,Technical Impact,Situated Impact",
        help="Names to use to identify the columns in -c. Comma-separated list.\
       Please don't use a header row in the input file.",
    )
    parser.add_option(
        "-p",
        "--priorities",
        type="string",
        default="Defer, Scheduled, Out-of-Cycle,Immediate",
        help="Ranked list, lowest to highest, of the labels for the decisions.\
       These need to match the values in the CVS file exactly.\
       Please input as a comma-separated list, no spaces. Current max is 5.",
    )
    ##############################################################################
    #### Set Boolean defaults
    parser.set_defaults(headerRow=True)
    ##############################################################################
    return parser


##########
## put other method definitions here
def print_preamble(location):
    """
    This just prints a reasonable latex preamble as a string literal.
    It's all hard-coded for now. Also begins the latex document.
    Note that \ u is interpreted as a unicode start symbol, even in trip quotes.
    \ a t and b have similar problems, and need to be escaped.
    """
    # standalone class instead of article as recommended here:
    # https://tex.stackexchange.com/questions/11866/compile-a-latex-document-into-a-png-image-thats-as-short-as-possible
    location.write(
        """
\documentclass[10pt,preview]{standalone}
\\usepackage[utf8]{inputenc}
\\usepackage[english]{babel}
\\usepackage{amsmath}
\\usepackage{amsfonts}
\\usepackage{amssymb}
\\usepackage[left=1.5cm,right=1.5cm,top=2cm,bottom=2cm,pdftex]{geometry}
\\usepackage{tikz}
\\usepackage[edges]{forest}
\\usetikzlibrary{arrows.meta}

\\author{Jonathan Spring}
\\title{Draft decision trees for vulnerability management}


\\begin{document}
\pagestyle{empty}
  """
    )


def print_forest_options(
    location, priorities=["Defer", "Scheduled", "Out-of-band", "Immediate"]
):
    """
    Global forest options, which are mostly the defs for the labels.
    Remember to escape the backslashes.
    As with print_preamble, there is limited flexibility here, but the names of
    the priority labels can be given as string inputs to the array "priorities"
    If the provided labels have special LaTeX characters, the method makes an
    effort to remove them.
    """
    while len(priorities) < 5:
        priorities.append("")
    # pad list. If it's too long, those labels just won't be used

    for i in range(len(priorities)):
        priorities[i] = re.sub(r"[_^$%&#{}\\]", "", priorities[i])
        # based on https://gist.github.com/jomigo96/6a040d4e4ad384bccd81c9a65e5cd210
        # this should remove the most common Latex control characters

    # There is a danger here that the decision labels may be processed as code
    # within the scope of the tikzset command
    # but doing this makes printing the right command easier, since it is
    # just the decision label in the graph is also the name of the style.
    pri1string = str(
        priorities[0]
        + "/.style={outcome, fill=gray, thick, draw=green, label=right:{"
        + priorities[0]
        + "}}\n"
    )
    pri2string = str(
        priorities[1]
        + "/.style={outcome, fill=yellow, thick, dashed, draw=yellow, label=right:{"
        + priorities[1]
        + "}}\n"
    )
    pri3string = str(
        priorities[2]
        + "/.style={outcome, fill=orange, thick, draw=orange, label=right:{"
        + priorities[2]
        + "}}\n"
    )
    pri4string = str(
        priorities[3]
        + "/.style={outcome, fill=red, thick, draw=black, label=right:{"
        + priorities[3]
        + "}}\n"
    )
    pri5string = str(
        priorities[4]
        + "/.style={outcome, fill=black, thick, dashed, draw=gray, label=right:{"
        + priorities[4]
        + "}}\n"
    )

    # write the forest options
    location.write(
        """
\\forestset{
my label/.style={edge label={node [pos=0.75,above,font=\scriptsize] {#1}} },
}
%
\\tikzset{
outcome/.style={shape=isosceles triangle,, shape border rotate=180, minimum height=0.4cm, minimum width=0.07cm}
}
\\tikzset{
"""
    )
    location.write(pri1string)
    location.write(
        """}
\\tikzset{
"""
    )
    location.write(pri2string)
    location.write(
        """}
\\tikzset{
"""
    )
    location.write(pri3string)
    location.write(
        """}
\\tikzset{
"""
    )
    location.write(pri4string)
    location.write(
        """}
\\tikzset{
"""
    )
    location.write(pri5string)
    location.write("}\n")  # close the last tikzset; forestset is already closed


def begin_forest(location):
    """This text begins a forest within the LaTeX document. These are
    options specific to this tree. This could be used multiple times in one
    LaTeX document, but if we are just going to have to split the PDF later
    then don't bother.  These have been tuned reasonably well, but could change.
    Make sure there are no empty lines between the begin and end statements.
    Escape backslashes.
    """
    location.write(
        """
\\footnotesize
\\noindent
\\begin{forest}
for tree={s sep*=0.33, l sep=20mm, child anchor=west, anchor=west, grow=east, calign=center, tier/.pgfmath=level()}, forked edges,
  """
    )


##############################################################################


def main():
    parser = initialize_options()
    (options, args) = parser.parse_args()
    f_iter = glob.glob(options.filelist)
    delim = options.delim
    if delim is not None:
        delimlen = len(delim)
    if options.out_file in ("-", "stdout"):
        ofile = sys.stdout
    else:
        ofile = open(options.out_file, "w")
    ##########
    ## recover other options here
    label = options.label
    columns = options.columns.split(",")
    depth = len(columns)  # depth of the tree
    for i in range(depth):
        columns[i] = int(columns[i])
    headerRow = options.headerRow
    if not headerRow:
        names = options.names.split(",")
    else:
        # if headerRow is true, need to recover names after file is read
        names = [None] * depth
    priorities = options.priorities.split(",")
    ##############################################################################

    ##########
    ## initialize variables here
    lines = []
    graph = {}
    dpoint_values = [[] for i in range(depth)]  # decision point values
    # creates an empty list to store decision values for each column
    sort_order = [[] for i in range(depth)]  # to preserve order in file
    counts = [0 for i in range(depth)]  # decision point values
    # tracking path traversal at each level of the tree
    tmp_path = []  # for tracking our place in the tree
    latex_brace_close = "] " + "\n"  # how we close a part of the tree in TeX
    ##############################################################################
    for file in f_iter:
        if file in ("-", "stdin"):
            handle = sys.stdin
            use_stdin = True
        else:
            handle = open(file, "r")
            use_stdin = False
        try:
            ##########
            ## read the input files here. To catch ingest errors, nest a try block
            lines = lines + handle.readlines()  # will need to strip whitespace
        finally:
            if not use_stdin:
                handle.close()

    ##########
    ## do whatever else you have to do here
    print_preamble(ofile)
    # This just prints the fairly static front matter.
    print_forest_options(location=ofile, priorities=priorities)
    # The labels for decisions are changable, these should be cmd line configs

    if headerRow:
        tmp_names = lines.pop(0).split(",")
        for i in range(depth):
            names[i] = tmp_names[columns[i]]
            # columns is the order the columns will be used, so make sure the
            # labels read from the file match that order

    for line in lines:
        path = []
        tmp = line.strip().split(delim)
        i = 0  # index for sort order matrix
        for col in columns:
            path.append(tmp[col])
            if tmp[col] not in sort_order[i]:
                sort_order[i].append(tmp[col])
            i += 1
        graph[tuple(path)] = tmp[label]
        # once we've constructed the path, to hash it it must be immutable

    paths = list(graph)
    for path in paths:
        for i in range(depth):
            if path[i] not in dpoint_values[i]:
                dpoint_values[i].append(path[i])
    for i in range(depth):
        dpoint_values[i].sort(key=lambda j: sort_order[i].index(j), reverse=True)
        # reverse because the latex will flip it again
        # loop twice so we don't sort every time we check a new path

    # Now take this "graph" structure and print the latex for the tree.
    begin_forest(ofile)

    ofile.write(str("[" + names[0] + ", rectangle, draw," + "\n"))
    # The root is special, and has no label. Only happens once.

    i = 0
    while i >= 0:
        outstring = ""
        if i == depth - 1:  # off by one error if we just test == depth
            # last layer needs to include decision labels
            for j in range(len(dpoint_values[i])):
                # this loop is for printing intermediate tree nodes (not root and not leaf)
                # The latex requires a nested structure just like the tree.
                label = dpoint_values[i][j]
                tmp_path.append(label)
                ofile.write(
                    "[, "
                    + graph[tuple(tmp_path)]
                    + ", my label={"
                    + label
                    + "} ]"
                    + "\n"
                )

                del tmp_path[-1]
            i = i - 1
            ofile.write(latex_brace_close)  # close each latex brace
            del tmp_path[-1]  # every time we close a brace, update the path to reflect
        else:  # "Normal" case
            if counts[i] == len(dpoint_values[i]):
                try:
                    del tmp_path[-1]
                except IndexError:
                    tmp_path = (
                        []
                    )  # basically this just allows us to reach the loop exit
                ofile.write(latex_brace_close)
                counts[i] = 0
                i = i - 1
                continue
            else:  # This section is for printing leaf labels
                current = counts[i]
                counts[i] += 1
                label = dpoint_values[i][current]
                tmp_path.append(label)
                outstring = str(
                    "["
                    + names[i + 1]
                    + ", rectangle, draw, my label={"
                    + label
                    + "},"
                    + "\n"
                )
                ofile.write(outstring)
                i += 1

    # ofile.write(latex_brace_close) # close the initial brace befoer the loop.
    # The last pass through the loop produces the requisite extra brace close
    ofile.write(str("\end{forest}" + "\n"))
    ofile.write(str("\end{document}" + "\n"))

    ##############################################################################

    ofile.close()
    print(
        """If everything went OK, then you should be able to create a PDF from \
the .tex file I just made by running:
  latexmk -pdf $file
Then you can remove all the extraneous latex files with:
  latexmk -c $file
You can also remove the .tex file, I can always make it again.
To make the PNG files for the HTML output document, use GhostScript:
  gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pngalpha -dBackgroundColor=16#ffffff -dMinFeatureSize=2 -sOutputFile=tree.png $pdf \
  """
    )
    # See https://www.ghostscript.com/doc/current/Devices.htm#PNG
    return 0  # if nothing goes wrong, return success for the exit code.


if __name__ == "__main__":
    main()
