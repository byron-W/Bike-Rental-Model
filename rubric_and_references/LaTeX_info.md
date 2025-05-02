# How to generate your document using LaTeX

## Summary of steps:

1.	Ensure all libraries are installed
  a.	Pandoc  
  b.	LaTeX  
  c.	Hyperref  
  d.	Style libraries: texlive-bibtex-extra  
  e.	Pandoc-citeproc  
2.	Create references.bib  
3.	Write your draft (draft.md)  
  a.	Insert references correctly  
  b.	View real time changes using ctrl+shift+v  
4.	Save draft.md, and convert as report.tex to LaTeX with references  
  a.	When report.tex is created, edit using the lines I give you below  
5.	Run the set of commands to convert to PDF.

## Steps detail:

1. Make sure you have necessary files installed:

- pandoc
```bash
sudo apt-get update
sudo apt-get install -y pandoc
```

- LaTeX (in CodeSpaces)
```bash
sudo apt-get update
sudo apt-get install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended texlive-bibtex-extra biber
```

- hyperref (may come with LaTeX, may not)
```bash
sudo apt-get install texlive-latex-extra
```

- style libraries for things like IEEE
```bash
sudo apt-get update
sudo apt-get install -y texlive-bibtex-extra
```

- if you want to put the citations in the markdown doc, then generate the tex doc you may need pandoc-citeproc
```bash
sudo apt-get install pandoc-citeproc
```
2. This is how your references.bib should look
```bash
@article{example2024,
  author  = {John Doe},
  title   = {An Example Paper},
  journal = {Journal of Examples},
  year    = {2024},
  volume  = {42},
  pages   = {1-10}
}
```

3. Create draft.md doc, then convert to report.tex doc using below command.   
  - a. Look up a reference for using Markdown if you aren't familiar with it  [Click here for markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/)
  - b. Examples for formatting:  
    - Headers are designated using hashes (1 hash for 1st level, 2 for 2nd, etc.)  
    - Force line breaks by putting two spaces at the end of a line, then hitting return.  
    - To show code, look at how I show the command below (using bash and `)  
    - Markdown cheat sheet also shows how to do URLs, footnotes, definition lists, highlighting and inserting images.
      
```bash
pandoc report/draft.md --citeproc --bibliography=report/references.bib -o report/report.tex
```

4. You will need to tweak the LaTeX doc before you try to turn it into a pdf. The doc will be produced missing some important lines at the start and end of the doc. Pandoc will produce your document with hyperlinked headers, but you need to manually call the hyperref package. Also, for some reason it misses document class, and the ending line. Below is what it should look like (I have removed some sections for brevity).
```bash
\documentclass{article}

% Packages
\usepackage{hyperref}  % Enable hyperlinks and hypertargets 

\begin{document}

\title{Final Report}
\author{Your Name}
\date{\today}

\maketitle

\hypertarget{final-report-title}{%
\section{Final Report Title}\label{final-report-title}}

\hypertarget{introduction}{%
\subsection{Introduction}\label{introduction}}

Background and objectives.

\hypertarget{discussion}{%
\subsection{Discussion}\label{discussion}}

Analysis and interpretations.

\hypertarget{references}{%
\subsection{References}\label{references}}

\hypertarget{refs}{}
\leavevmode\hypertarget{ref-example2024}{}%
Doe, John. 2024. ``An Example Paper.'' \emph{Journal of Examples} 42
(1): 1--10.

\end{document}
```

5. This is the set of commands you need to turn tex doc to pdf (yes, some lines are run more than once). Note that the output folder is specified, else the resulting docs will wind up in the root folder and bibtex won't be able to find them.
```bash
pdflatex -output-directory=report report/report.tex
bibtex report/report
pdflatex -output-directory=report report/report.tex
pdflatex -output-directory=report report/report.tex
```

