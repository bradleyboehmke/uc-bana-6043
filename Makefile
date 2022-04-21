SOURCE     = ./book
TARGET     = ./docs

my_book:
	@echo "Building book..."
	@jupyter-book build --path-output $(TARGET) $(SOURCE)
