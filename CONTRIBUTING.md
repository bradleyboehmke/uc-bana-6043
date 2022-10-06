# Contributing Guide

The material on this site is written in Jupyter notebooks and rendered using [Jupyter Book](https://jupyterbook.org/intro.html) to make it easily accessible. If you'd like to contribute then:

1. Clone the GitHub repository:
   ```sh
   git clone https://github.com/bradleyboehmke/uc-bana-6043.git
   ```
2. Create a new branch to make your changes in:
   ```sh
   git checkout -b <your-branch-name>
   ```
3. Install the conda environment by typing the following in your terminal:
   ```sh
   conda env create -f bana6043.yaml
   ```
4. Open the course in JupyterLab or any other editor by typing the following in your terminal:
   ```sh
   cd uc-bana-6043
   
   # open in JupyterLab 
   jupyterlab

   # or open in VS code
   code .
   ```
5. Make your changes/additions to the book content. All book content is located in the `book/` directory. Once you've saved your changes rebuild the book and view your changes. The HTML book content is automatically created and stored in the `docs/` directory.
   ```sh
   # rebuild book 
   make my_book

   # view rebuilt book
   make open_book
   ```
6. If satisfied with your changes commit and push your changes to Github and open a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
   ```sh
   git add <files you changed>
   git commit -m <informative commit message>
   git push -u origin <your-branch-name>
   ```