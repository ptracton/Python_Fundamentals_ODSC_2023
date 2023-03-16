
LECTURE_ROOT = python_fundamentals


LECTURE_SRC = $(LECTURE_ROOT).tex
LECTURE_PDF = $(LECTURE_ROOT).pdf


##
## Tools
##
LATEX = pdflatex
DVIPDF = dvipdf 
RM = /bin/rm
MV = /bin/mv
MKDIR = /bin/mkdir
GLOSSARY = makeglossaries

##
## Directories
##
SRC_DIR = .
OUTPUT_DIR = .
LECTURE_OUTPUT_DIR = .

MAKE_DIRS = $(OUTPUT_DIR)

BUILD_LIST = lecture

LATEX_OPTIONS = -shell-escape

all: $(BUILD_LIST)

lecture: 
	$(MKDIR) -p $(LECTURE_OUTPUT_DIR)
	$(MKDIR) -p $(OUTPUT_DIR)
	$(LATEX) $(LATEX_OPTIONS) -output-directory=$(OUTPUT_DIR) $(SRC_DIR)/$(LECTURE_SRC)	
	$(GLOSSARY) $(LECTURE_ROOT).acn
	$(LATEX) $(LATEX_OPTIONS) -output-directory=$(OUTPUT_DIR) $(SRC_DIR)/$(LECTURE_SRC)	

clean:
	find . -name "*~" | xargs $(RM) -f
	$(RM) -rf *.pdf
	$(RM) -rf auto *.acn *.aux *.glo *.ist *.lof *.log *.lol *.lot
	$(RM) -rf *.out *.snippets *.toc
	$(RM) -rf _minted*
