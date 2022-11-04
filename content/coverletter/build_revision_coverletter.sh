cat coverletter_revision.md ../../reviews/elife_answers.md > assm.md

pandoc --pdf-engine=tectonic --template=template-letter.tex assm.md -o coverletter_revision.pdf