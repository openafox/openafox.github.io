---
layout: post
title: Bulk Doc to Docx Conversion
tag:
    - Data Engineering
    - Legacy Software
category: Programming

excerpt: Docx can be parsed Doc can't. Bulk convert using a VBA script.
---
This [Microsoft forum post](https://answers.microsoft.com/en-us/msoffice/forum/msoffice_word-mso_win10-mso_o365b/bulk-convert-doc-files-to-docx-in-word-2016/1c5628bc-c2ea-4072-bb25-56eae952d2c5) pretty much explains it but I'm gonna restate here.

In a VBA Module:

```
Sub TranslateDocIntoDocx()
  Dim objWordApplication As New Word.Application
  Dim objWordDocument As Word.Document
  Dim strFile As String
  Dim strFolder As String

  strFolder = "D:\doc\"
  strFile = Dir(strFolder & "*.doc", vbNormal)

  While strFile <> ""
    With objWordApplication
      Set objWordDocument = .Documents.Open(FileName:=strFolder &strFile, AddToRecentFiles:=False, ReadOnly:=True, Visible:=False)

      With objWordDocument
        .SaveAs FileName:=strFolder & Replace(strFile, "doc", "docx"), FileFormat:=16
        .Close
      End With
    End With
    strFile = Dir()
  Wend

  Set objWordDocument = Nothing
  Set objWordApplication = Nothing
End Sub
```
Replace `"D:\doc\"` with your file path. Remember to include the trailing "\\".

If your path is wrong it will not tell you.  It may do some weird multi docxx
creation. Script could use some updates. I may look into updating it if I have
to use it again.
