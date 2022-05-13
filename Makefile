SOURCE     = ./book
TARGET     = ./docs
BOOK       = ./docs/_build/html/index.html

my_book:
	@echo "Building book..."
	@jupyter-book build --path-output $(TARGET) $(SOURCE)

clean_cache:
	@echo "Clearing cached files..."
	@jupyter-book clean $(TARGET) --all

open_book:
	@open $(BOOK)
