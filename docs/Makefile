.PHONY: default
default: eco.dot.svg glossary.md.html todo.md.html

%.dot.svg: %.dot
	dot -T svg -o $@ $<

%.md.html: %.md
	markdown > $@ $<
