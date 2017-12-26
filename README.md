# MySQL Workbench HTML Document Generation

A Python script to generate HTML documentation from MySQL Workbench ERR diagram.
Original version for generating Markdown-docs from models by Hieu Le Trung you find [here](https://github.com/letrunghieu/mysql-workbench-plugin-doc-generating).


## Installation

* Download the latest version from [Github](https://github.com/d1soft/mysql-workbench-html-doc-generator)
* Extract the downloaded file and find a file named `d1-diagram-html-doc-generator.py`
* Open the MySQL Workbench
* Navigate to menu **Scripting** > **Install Plugin/Module...**
* Browse and select the extracted `.py` file
* Restart the Workbench

## Usage

### Generate documentation from diagram

* Open the ERR digram
* Navigate to menu **Tools** > **Utilities** > **Generate Documentation (HTML)**
* When you see the status bar text changed to *Documentation generated into the clipboard. Paste it to your editor.*, Paste (<kbd>Ctrl</kbd> + <kbd>V</kbd> in most Linux/Window applications) to your editor and save as a new file.

### Generate ERR digram from physical database

In case that you do not have the ERR diagram, you have to create a diagram from your physical database first. Don't worry, MySQL Workbench has a greate tool to do this for you called **Reverse Engineer**.

* Open Workbench
* Navigate to menu **Database** > **Reverse Engineer...**
* Choose the connection, **Next**
* Wait and **Next**
* Select the datbase you want to create ERR diagram from, **Next**
* Wait and **Next**
* Select tables that you want to include in the ERR diagram, **Execute>**
* Wait and **Next**
* **Finish**

You have a new ERR diagram, you can generate the documentation from this diagram as the previous step.

### Features

* Autogenerating contents.
* Autogenerating anchors from FKs to tables.
* Tables and columns description generates from comments.

## License

This script is released under the MIT license.
Original description by Hieu Le Trung.
