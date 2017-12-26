# MySQL Workbench Plugin
# <description>
# Written in MySQL Workbench 6.3.4
# -*- coding: utf-8 -*-

from wb import *
import grt
import mforms

ModuleInfo = DefineModule("ModelHtmlDocumentation", author="d1", version="1.0.0", description="Generate HTML documentation from a model")

# This plugin takes no arguments
@ModuleInfo.plugin("info.d1.wb.htmldocgen", caption="Generate documentation (HTML)", description="description", input=[wbinputs.currentDiagram()], pluginMenu="Utilities")
@ModuleInfo.export(grt.INT, grt.classes.db_Catalog)
def documentation(diagram):
    glossary = "<html><head><style>TD,TH{padding:3px;border:1px solid #000;}TH{text-align: left; border: 1px solid #000;}</style></head><body><h1 id=\"d1_doc_gen_contents\">Contents</h1>\n\n<ul>"
    text = "<h1>Tables</h1>\n\n"

    
    for figure in diagram.figures:
        if hasattr(figure, "table") and figure.table:
            text += writeTableDoc(figure.table)
            glossary += writeGlossary(figure.table)

    glossary += "</ul>"
    mforms.Utilities.set_clipboard_text(glossary + text + "</body></html>")
    mforms.App.get().set_status_text("Documentation generated into the clipboard. Paste it to your editor.")

    print "Documentation is copied to the clipboard."
    return 0

def writeTableDoc(table):
    text = "<h2 id=\"" + table.name + "\"> Table: <code>" + table.name + "</code></h2>\n\n"

    text += "<h3>Description:</h3>\n\n"

    text += "<p>" + table.comment + "</p>\n\n"

    text += "<h3>Columns:</h3>\n\n"

    text += "<table><thead><tr class=\"header\">"

    text += "<th align=\"left\">Column</th><th align=\"left\">Data type</th><th align=\"left\">Attribute</th><th align=\"left\">Defualt</th><th align=\"left\">Description</th></tr></thead><tbody>\n\n"

    for column in table.columns:
        text += writeColumnDoc(column, table)

    text += "</tbody></table>\n\n"

    if (len(table.indices)):
        text += "<h3>Indexes:</h3>\n\n"
    
    text += "<table><thead><tr class=\"header\">"

    text += "<th align=\"left\">Name</th><th align=\"left\">Columns</th><th align=\"left\">Data type</th><th align=\"left\">Description</th></tr></thead><tbody>\n\n"

    for index in table.indices:
            text += writeIndexDoc(index)

    text += "</tbody></table><a href=\"#d1_doc_gen_contents\">To contents</a>\n\n"

    return text

def writeGlossary(table):
	return "<li><a href=\"#" + table.name + "\"><b>" + table.name + "</b></a></li>\n"
	
def writeColumnDoc(column, table):
    # column name
    text = "<tr><td><code>" + column.name + "</code></td>"

    # column type name
    if column.simpleType:
        text += "<td>" + column.simpleType.name 
        # column max lenght if any
        if column.length != -1:
            text += "(" + str(column.length) + ")"
    else:
        text += "<td>"

    

    text += "</td><td>"

    # column attributes
    attribs = [];

    isPrimary = False;
    isUnique = False;
    for index in table.indices:
        if index.indexType == "PRIMARY":
            for c in index.columns:
                if c.referencedColumn.name == column.name:
                    isPrimary = True
                    break
        if index.indexType == "UNIQUE":
            for c in index.columns:
                if c.referencedColumn.name == column.name:
                    isUnique = True
                    break

    # primary?
    if isPrimary:
        attribs.append("PRIMARY")

    # auto increment?
    if column.autoIncrement == 1:
        attribs.append("AUTO INCREMENTS")

    # not null?
    if column.isNotNull == 1:
        attribs.append("NOT NULL")

    # unique?
    if isUnique:
        attribs.append("UNIQUE")

    text += ", ".join(attribs)

    # column default value
    text += "</td><td>" + (("<code>" + column.defaultValue + "</code>") if column.defaultValue else " ")

    # column description
    text += "</td><td>" + (nl2br(column.comment) if column.comment else " ")

    # foreign key
    for fk in table.foreignKeys:
        if fk.columns[0].name == column.name:
            text +=  ("<br /><br />" if column.comment else "") + "FK in column <code>" + fk.referencedColumns[0].name + "</code> in table <a href=\"#" + fk.referencedColumns[0].owner.name + "\"><code>" + fk.referencedColumns[0].owner.name + "</code></a>."
            break


    # finish
    text  +=  "</td></tr>" + "\n"
    return text

def writeIndexDoc(index):

    # index name
    text = "<tr><td>" + index.name

    # index columns
    text += "</td><td>" + ", ".join(map(lambda x: "<code>" + x.referencedColumn.name + "</code>", index.columns))

    # index type
    text += "</td><td>" + index.indexType

    # index description
    text += "</td><td>" + (nl2br(index.comment) if index.comment else " ")

    # finish
    text += "</td></tr>\n"

    return text

def nl2br(text):
    return "<br />".join(map(lambda x: x.strip(), text.split("\n")))
