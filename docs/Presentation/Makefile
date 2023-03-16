
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

##
## Directories
##
SRC_DIR = src
OUTPUT_DIR = outputs
LECTURE_OUTPUT_DIR = .

MAKE_DIRS = $(OUTPUT_DIR)

BUILD_LIST = lecture

LATEX_OPTIONS = -shell-escape

all: $(BUILD_LIST)

lecture: 
	$(MKDIR) -p $(LECTURE_OUTPUT_DIR)
	$(MKDIR) -p $(OUTPUT_DIR)
	$(LATEX) $(LATEX_OPTIONS) -output-directory=$(OUTPUT_DIR) $(SRC_DIR)/$(LECTURE_SRC)	
	$(LATEX) $(LATEX_OPTIONS) -output-directory=$(OUTPUT_DIR) $(SRC_DIR)/$(LECTURE_SRC)
	$(MV) $(OUTPUT_DIR)/$(LECTURE_PDF) $(LECTURE_OUTPUT_DIR)	

clean:
	$(RM) -rf $(OUTPUT_DIR)
	find . -name "*~" | xargs $(RM) -f
	$(RM) -rf $(LECTURE_OUTPUT_DIR)/$(LECTURE_PDF)
	$(RM) -rf _minted*
